"""
Blind Assist Application

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Main application entry point.
    Handles application flow, object detection,
    user interaction, and audio feedback.

Copyright (c) 2026
"""
"""
main.py

Blind Assist Application

Main execution loop.

"""

from maix import app, time

from config import (
    CONFIDENCE_THRESHOLD,
    IOU_THRESHOLD,
    COOLDOWN_MS,
    BUTTON_DEBOUNCE_MS,
)

from hardware import initialize_hardware

from distance import (
    estimate_distance,
    format_distance,
)

from audio_utils import announce_detection

from ui import (
    draw_exit_button,
    draw_detection_box,
    draw_detection_label,
    draw_detection_status,
)

from utils import is_in_button


# =============================================================================
# Hardware Initialization
# =============================================================================

hw = initialize_hardware()


# =============================================================================
# Runtime Variables
# =============================================================================

last_label = None
last_play_time = 0

button_prev_state = hw.button.value()
detection_enabled = False

print("System ready. Press physical button to toggle detection.")


# =============================================================================
# Main Loop
# =============================================================================

while not app.need_exit():

    # -----------------------------------------------------------------
    # Capture Image
    # -----------------------------------------------------------------

    img = hw.camera.read()

    # -----------------------------------------------------------------
    # Exit Button
    # -----------------------------------------------------------------

    exit_button = draw_exit_button(img)

    x, y, pressed = hw.touchscreen.read()

    if pressed and is_in_button(x, y, exit_button):
        app.set_exit_flag(True)

    # -----------------------------------------------------------------
    # Physical Button
    # -----------------------------------------------------------------

    button_state = hw.button.value()

    if button_prev_state == 1 and button_state == 0:

        detection_enabled = not detection_enabled

        print(
            f"Detection {'ENABLED' if detection_enabled else 'DISABLED'}"
        )

        hw.led.value(int(detection_enabled))

        time.sleep_ms(BUTTON_DEBOUNCE_MS)

    button_prev_state = button_state

    # -----------------------------------------------------------------
    # Detection Disabled
    # -----------------------------------------------------------------

    if not detection_enabled:

        draw_detection_status(
            img,
            False,
        )

        hw.display.show(img)

        continue

    # -----------------------------------------------------------------
    # Object Detection
    # -----------------------------------------------------------------

    detections = hw.detector.detect(
        img,
        conf_th=CONFIDENCE_THRESHOLD,
        iou_th=IOU_THRESHOLD,
    )

    if detections:

        for obj in detections:

            draw_detection_box(
                img,
                obj,
            )

            label = hw.detector.labels[obj.class_id]

            score = obj.score

            distance = estimate_distance(
                obj.w,
                hw.detector.input_width(),
            )

            distance_label = format_distance(distance)

            draw_detection_label(
                img,
                obj,
                label,
                score,
                distance,
            )

            current_time = time.ticks_ms()

            if (
                label != last_label
                or
                time.ticks_diff(
                    current_time,
                    last_play_time,
                ) > COOLDOWN_MS
            ):

                announce_detection(
                    hw.player,
                    label,
                    distance_label,
                )

                last_label = label
                last_play_time = current_time

    else:

        last_label = None

    # -----------------------------------------------------------------
    # Draw Detection Status
    # -----------------------------------------------------------------

    draw_detection_status(
        img,
        True,
    )

    hw.display.show(img)


# =============================================================================
# Cleanup
# =============================================================================

hw.camera.close()
hw.display.close()