"""
Blind Assist Application

Author(s):
    Revanth A H
    Parthavi N R

Description:
    General utility functions used throughout
    the Blind Assist application.

Copyright (c) 2026
"""

"""
utils.py

General helper functions used throughout the Blind Assist application.
"""

# =============================================================================
# Button Utilities
# =============================================================================

def is_in_button(
    x,
    y,
    button_rect,
):
    """
    Check whether a touchscreen coordinate lies inside a button.

    Parameters
    ----------
    x : int
        Touch X coordinate.

    y : int
        Touch Y coordinate.

    button_rect : list
        Rectangle in the format:
        [x, y, width, height]

    Returns
    -------
    bool
        True if the point is inside the rectangle.
    """

    return (
        button_rect[0] < x < button_rect[0] + button_rect[2]
        and
        button_rect[1] < y < button_rect[1] + button_rect[3]
    )