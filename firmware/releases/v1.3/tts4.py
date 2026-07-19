from maix import camera, pinmap, display, touchscreen, image, nn, app, audio, time, gpio
import os

# --- Load YOLOv11 model ---
detector = nn.YOLO11(model="/root/models/yolo11n.mud", dual_buff=True)

# --- Initialize camera and display ---
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
disp = display.Display()
ts = touchscreen.TouchScreen()

# --- Initialize audio player ---
player = audio.Player()

# --- Button setup (active LOW) ---
button_pin = gpio.GPIO("A19", mode=gpio.Mode.IN, pull=gpio.Pull.PULL_UP)

pinmap.set_pin_function("A18", "GPIOA18")
led = gpio.GPIO("GPIOA18", gpio.Mode.OUT)
led_value = 0
led.value(0)

# --- Variables ---
last_label = None
last_play_time = 0
cooldown_ms = 1000
button_prev_state = 0
detection_enabled = False  # Start OFF

# --- Camera/Lens parameters for distance estimation ---
FOCAL_LENGTH_MM = 4.37
SENSOR_WIDTH_MM = 6.4
DEFAULT_WIDTH_M = 0.5  # fallback width if label not found

# --- Load object widths (already in meters) ---
object_widths = {}
try:
    with open("/root/avg.txt", "r") as f:
        for line in f:
            if ":" in line:
                label, value = line.strip().split(":")
                num = float(value.replace("m", "").strip())
                object_widths[label.strip().lower()] = num
    print("Loaded object widths:", object_widths)
except Exception as e:
    print("Failed to load avg.txt:", e)

def is_in_button(x, y, btn_pos):
    return x > btn_pos[0] and x < btn_pos[0] + btn_pos[2] and y > btn_pos[1] and y < btn_pos[1] + btn_pos[3]

def play_wav(file_path, volume=5):
    """Play a .wav file asynchronously"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        player.volume(volume)
        player.play(data)
    except Exception as e:
        print(f"Audio play failed: {e}")

print("System ready. Press physical button to toggle detection.")

while not app.need_exit():
    img = cam.read()

    # --- Touchscreen Exit Button ---
    exit_label = "< Exit"
    size = image.string_size(exit_label)
    exit_btn_pos = [0, 0, 8 * 2 + size.width(), 12 * 2 + size.height()]
    img.draw_string(8, 12, exit_label, image.COLOR_WHITE)
    img.draw_rect(exit_btn_pos[0], exit_btn_pos[1], exit_btn_pos[2], exit_btn_pos[3], image.COLOR_WHITE, 2)

    x, y, pressed = ts.read()
    if is_in_button(x, y, exit_btn_pos):
        app.set_exit_flag(True)

    # --- Button Toggle Logic ---
    button_state = button_pin.value()
    if button_prev_state == 1 and button_state == 0:
        detection_enabled = not detection_enabled
        print(f"Detection {'ENABLED' if detection_enabled else 'DISABLED'}")
        led_value = not led_value
        led.value(led_value)
        time.sleep_ms(300)
    button_prev_state = button_state

    # --- If detection disabled, show message only ---
    if not detection_enabled:
        img.draw_string(100, 20, "Detection: OFF", color=image.COLOR_RED, scale=1.5)
        disp.show(img)
        continue

    # --- YOLO Detection ---
    objs = detector.detect(img, conf_th=0.8, iou_th=0.75)
    if objs:
        for obj in objs:
            img.draw_rect(obj.x, obj.y, obj.w, obj.h, color=image.COLOR_RED)

            label = detector.labels[obj.class_id]
            score = obj.score

            # --- Distance Estimation using label-specific width ---
            known_width = object_widths.get(label.lower(), DEFAULT_WIDTH_M)
            distance_m = (known_width * FOCAL_LENGTH_MM * detector.input_width()) / (obj.w * SENSOR_WIDTH_MM)
            distance_m = max(0.1, min(distance_m, 10.0))

            if distance_m <= 1.0:
                distance_rounded = round(distance_m, 1)
                distance_label = f"{distance_rounded:.1f}m"
            else:
                distance_rounded = round(distance_m * 2) / 2
                distance_label = f"{int(distance_rounded)}m" if distance_rounded.is_integer() else f"{distance_rounded}m"

            msg = f"{label}: {score:.2f}, {distance_m:.2f}m"
            print(msg)
            img.draw_string(obj.x, obj.y, msg, color=image.COLOR_RED)

            # --- Audio Feedback ---
            current_time = time.ticks_ms()
            if label != last_label or (time.ticks_diff(current_time, last_play_time) > cooldown_ms):
                label_path = f"/root/detected_audio_48k/{label}.wav"
                distance_path = f"/root/detected_audio_48k/{distance_label}.wav"

                if os.path.exists(label_path):
                    play_wav(label_path, volume=5)
                    time.sleep_ms(200)

                if os.path.exists(distance_path):
                    play_wav(distance_path, volume=5)
                else:
                    print(f"No sound file for {distance_label}")

                last_label = label
                last_play_time = current_time
    else:
        last_label = None

    img.draw_string(100, 20, "Detection: ON", color=image.COLOR_GREEN, scale=1.5)
    led.value(1)
    disp.show(img)

cam.close()
disp.close()
