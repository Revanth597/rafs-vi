from maix import camera, display, image, nn, app, audio, time
import os

# Load YOLOv11 model
detector = nn.YOLO11(model="/root/models/yolo11n.mud", dual_buff=True)

# Initialize camera and display
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
disp = display.Display()

# Initialize audio player
player = audio.Player()

last_label = None
last_play_time = 0
cooldown_ms = 1500  # 1.5 seconds between same sounds

def play_wav(file_path, volume=50):
    """Play a .wav file asynchronously (non-blocking)"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        player.volume(volume)
        player.play(data)  # feed raw bytes directly (no Bytes wrapper)
    except Exception as e:
        print(f"Audio play failed: {e}")

while not app.need_exit():
    img = cam.read()
    objs = detector.detect(img, conf_th=0.5, iou_th=0.45)

    if objs:
        for obj in objs:
            # Draw detection boxes and labels
            img.draw_rect(obj.x, obj.y, obj.w, obj.h, color=image.COLOR_RED)
            label = detector.labels[obj.class_id]
            msg = f"{label}: {obj.score:.2f}"
            img.draw_string(obj.x, obj.y, msg, color=image.COLOR_RED)

            # Handle cooldown logic
            current_time = time.ticks_ms()
            if label != last_label or (time.ticks_diff(current_time, last_play_time) > cooldown_ms):
                file_path = f"/root/Sounds/{label}.wav"
                if os.path.exists(file_path):
                    play_wav(file_path, volume=80)
                    last_label = label
                    last_play_time = current_time  # ✅ fixed variable name
                else:
                    print(f"No sound file for {label}")
    else:
        last_label = None

    disp.show(img)
