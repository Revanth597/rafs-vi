"""
Blind Assist Application

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Provides distance estimation and distance
    formatting utilities for detected objects.

Copyright (c) 2026
"""
"""
distance.py

Distance estimation utilities for the Blind Assist application.

This module estimates object distance using a single default object width.
"""

from config import (
    FOCAL_LENGTH_MM,
    SENSOR_WIDTH_MM,
    DEFAULT_OBJECT_WIDTH_M,
)


# =============================================================================
# Distance Estimation
# =============================================================================

def estimate_distance(
    object_pixel_width,
    detector_input_width,
):
    """
    Estimate object distance using the pinhole camera model.

    Parameters
    ----------
    object_pixel_width : int
        Width of the detected bounding box in pixels.

    detector_input_width : int
        Width of the detector input image.

    Returns
    -------
    float
        Estimated distance in meters.
    """

    distance = (
        DEFAULT_OBJECT_WIDTH_M
        * FOCAL_LENGTH_MM
        * detector_input_width
    ) / (
        object_pixel_width
        * SENSOR_WIDTH_MM
    )

    # Clamp distance
    distance = max(0.1, min(distance, 10.0))

    return distance


# =============================================================================
# Distance Formatting
# =============================================================================

def format_distance(distance):
    """
    Convert the estimated distance into the corresponding
    audio filename.

    Examples
    --------
    0.84 -> "0.8m"
    2.1  -> "2m"
    2.3  -> "2.5m"
    """

    if distance <= 1.0:
        rounded = round(distance, 1)
        return f"{rounded:.1f}m"

    rounded = round(distance * 2) / 2

    if rounded.is_integer():
        return f"{int(rounded)}m"

    return f"{rounded}m"