from maix import camera, display, touchscreen, image, nn, app, audio, time
import os

# Load YOLOv11 model
detector = nn.YOLO11(model="/root/models/yolo11n.mud", dual_buff=True)

# Initialize camera and display
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
disp = display.Display()
ts = touchscreen.TouchScreen()

# Initialize audio player
player = audio.Player()

last_label = None
last_play_time = 0
cooldown_ms = 1000  # 1 second cooldown


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


while not app.need_exit():
    img = cam.read()
    objs = detector.detect(img, conf_th=0.8, iou_th=0.75)

    # Draw exit button
    exit_label = "< Exit"
    size = image.string_size(exit_label)
    exit_btn_pos = [0, 0, 8 * 2 + size.width(), 12 * 2 + size.height()]
    img.draw_string(8, 12, exit_label, image.COLOR_WHITE)
    img.draw_rect(exit_btn_pos[0], exit_btn_pos[1], exit_btn_pos[2], exit_btn_pos[3], image.COLOR_WHITE, 2)
    x, y, pressed = ts.read()
    if is_in_button(x, y, exit_btn_pos):
        app.set_exit_flag(True)

    if objs:
        for obj in objs:
            # Draw detection box
            img.draw_rect(obj.x, obj.y, obj.w, obj.h, color=image.COLOR_RED)

            label = detector.labels[obj.class_id]
            score = obj.score

            # --- Distance Estimation ---
            focal_length_mm = 3.8
            sensor_width_mm = 5.0
            known_width_m = 0.5

            distance_m = (known_width_m * focal_length_mm) / (obj.w * (sensor_width_mm / detector.input_width()))
            distance_m = max(0.1, min(distance_m, 10.0))  # Clamp 0.1–10 m

            # --- Distance Rounding ---
            if distance_m <= 1.0:
                # Round to nearest 0.1 m below 1 meter
                distance_rounded = round(distance_m, 1)
                distance_label = f"{distance_rounded:.1f}m"
            else:
                # Round to nearest 0.5 m above 1 meter
                distance_rounded = round(distance_m * 2) / 2
                distance_label = f"{int(distance_rounded)}m" if distance_rounded.is_integer() else f"{distance_rounded}m"

            # --- Draw label + probability + distance ---
            msg = f"{label}: {score:.2f}, {distance_m:.2f}m"
            print(msg)
            img.draw_string(obj.x, obj.y, msg, color=image.COLOR_RED)

            # --- Audio Feedback with Cooldown ---
            current_time = time.ticks_ms()
            if label != last_label or (time.ticks_diff(current_time, last_play_time) > cooldown_ms):
                label_path = f"/root/detected_audio_48k/{label}.wav"
                distance_path = f"/root/detected_audio_48k/{distance_label}.wav"

                # Play label audio (e.g. person.wav)
                if os.path.exists(label_path):
                    play_wav(label_path, volume=5)
                    time.sleep_ms(300)

                # Play distance audio (e.g. 0.4m.wav or 2m.wav)
                if os.path.exists(distance_path):
                    play_wav(distance_path, volume=5)
                else:
                    print(f"No sound file for {distance_label}")

                last_label = label
                last_play_time = current_time

    else:
        last_label = None

    disp.show(img)
