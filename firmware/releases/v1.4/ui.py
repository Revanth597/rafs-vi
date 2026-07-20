"""
ui.py

User interface helper functions for the Blind Assist application.

This module contains every drawing function used by the application.

Responsibilities
----------------
• Draw Exit Button
• Draw Detection Status
• Draw Bounding Boxes
• Draw Detection Labels
"""

from maix import image

from config import (
    EXIT_BUTTON_TEXT,
    EXIT_TEXT_X,
    EXIT_TEXT_Y,
    STATUS_TEXT_X,
    STATUS_TEXT_Y,
    STATUS_TEXT_SCALE,
    COLOR_UI,
    COLOR_DETECTION,
    COLOR_STATUS_ON,
    COLOR_STATUS_OFF,
)


# =============================================================================
# Exit Button
# =============================================================================

def draw_exit_button(img):
    """
    Draw the touchscreen exit button.

    Returns
    -------
    list
        Button rectangle in the format:
        [x, y, width, height]
    """

    text_size = image.string_size(EXIT_BUTTON_TEXT)

    button = [
        0,
        0,
        EXIT_TEXT_X * 2 + text_size.width(),
        EXIT_TEXT_Y * 2 + text_size.height(),
    ]

    img.draw_string(
        EXIT_TEXT_X,
        EXIT_TEXT_Y,
        EXIT_BUTTON_TEXT,
        COLOR_UI,
    )

    img.draw_rect(
        button[0],
        button[1],
        button[2],
        button[3],
        COLOR_UI,
        2,
    )

    return button


# =============================================================================
# Detection Status
# =============================================================================

def draw_detection_status(
    img,
    detection_enabled,
):
    """
    Draw detection ON/OFF status.
    """

    if detection_enabled:

        text = "Detection: ON"
        color = COLOR_STATUS_ON

    else:

        text = "Detection: OFF"
        color = COLOR_STATUS_OFF

    img.draw_string(
        STATUS_TEXT_X,
        STATUS_TEXT_Y,
        text,
        color=color,
        scale=STATUS_TEXT_SCALE,
    )


# =============================================================================
# Bounding Box
# =============================================================================

def draw_detection_box(
    img,
    obj,
):
    """
    Draw bounding box around a detected object.
    """

    img.draw_rect(
        obj.x,
        obj.y,
        obj.w,
        obj.h,
        color=COLOR_DETECTION,
    )


# =============================================================================
# Detection Label
# =============================================================================

def draw_detection_label(
    img,
    obj,
    label,
    confidence,
    distance,
):
    """
    Draw detection text above the object.
    """

    message = (
        f"{label}: "
        f"{confidence:.2f}, "
        f"{distance:.2f}m"
    )

    img.draw_string(
        obj.x,
        obj.y,
        message,
        color=COLOR_DETECTION,
    )