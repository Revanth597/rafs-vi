"""
hardware.py

Hardware initialization for the Blind Assist application.

This module initializes all hardware peripherals required by the
application and returns them as a single Hardware any.
"""

from dataclasses import dataclass

from maix import (
    camera,
    display,
    touchscreen,
    nn,
    audio,
    gpio,
    pinmap,
)

from config import (
    MODEL_PATH,
    BUTTON_PIN,
    LED_PIN,
)


@dataclass
class Hardware:
    """
    Container holding all initialized hardware interfaces.
    """

    detector: any
    camera: any
    display: any
    touchscreen: any
    player: any
    button: any
    led: any


def initialize_hardware() -> Hardware:
    """
    Initialize every hardware peripheral used by the application.

    Returns
    -------
    Hardware
        Initialized hardware interfaces.
    """

    # -------------------------------------------------------------
    # Object Detector
    # -------------------------------------------------------------

    detector = nn.YOLO11(
        model=MODEL_PATH,
        dual_buff=True,
    )

    # -------------------------------------------------------------
    # Camera
    # -------------------------------------------------------------

    cam = camera.Camera(
        detector.input_width(),
        detector.input_height(),
        detector.input_format(),
    )

    # -------------------------------------------------------------
    # Display
    # -------------------------------------------------------------

    disp = display.Display()

    # -------------------------------------------------------------
    # Touchscreen
    # -------------------------------------------------------------

    ts = touchscreen.TouchScreen()

    # -------------------------------------------------------------
    # Audio
    # -------------------------------------------------------------

    player = audio.Player()

    # -------------------------------------------------------------
    # Push Button
    #
    # Keep the button active LOW with an internal pull-up.
    # This matches the behaviour of the original application.
    # -------------------------------------------------------------

    button = gpio.GPIO(
        BUTTON_PIN,
        mode=gpio.Mode.IN,
        pull=gpio.Pull.PULL_UP,
    )

    # -------------------------------------------------------------
    # Status LED
    # -------------------------------------------------------------

    pinmap.set_pin_function(LED_PIN, "GPIOA18")

    led = gpio.GPIO(
        "GPIOA18",
        gpio.Mode.OUT,
    )

    led.value(0)

    # -------------------------------------------------------------
    # Return Hardware Object
    # -------------------------------------------------------------

    return Hardware(
        detector=detector,
        camera=cam,
        display=disp,
        touchscreen=ts,
        player=player,
        button=button,
        led=led,
    )