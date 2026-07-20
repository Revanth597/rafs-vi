"""
Blind Assist Application

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Central configuration file containing
    application constants and hardware settings.

Copyright (c) 2026
"""

"""
config.py

Configuration settings for the Blind Assist application.

This module contains all application-wide constants including
model configuration, GPIO mappings, UI settings, camera calibration,
audio settings, and detection parameters.

No application logic should be written in this file.
"""

from maix import image

# =============================================================================
# Model Configuration
# =============================================================================

MODEL_PATH = "/root/models/yolo11n.mud"

# =============================================================================
# Audio Configuration
# =============================================================================

OBJECT_AUDIO_DIR = "/root/audios/objects"
DISTANCE_AUDIO_DIR = "/root/audios/distance"

DEFAULT_AUDIO_VOLUME = 5
AUDIO_GAP_MS = 200

# =============================================================================
# YOLO Detection
# =============================================================================

CONFIDENCE_THRESHOLD = 0.80
IOU_THRESHOLD = 0.75

# =============================================================================
# Camera Calibration
# =============================================================================

FOCAL_LENGTH_MM = 4.37
SENSOR_WIDTH_MM = 6.4

# Default object width used for distance estimation (meters)
DEFAULT_OBJECT_WIDTH_M = 0.5

# =============================================================================
# Timing Parameters (milliseconds)
# =============================================================================

COOLDOWN_MS = 1000
BUTTON_DEBOUNCE_MS = 300

# =============================================================================
# GPIO Configuration
# =============================================================================

BUTTON_PIN = "A19"
LED_PIN = "A18"

# =============================================================================
# User Interface
# =============================================================================

EXIT_BUTTON_TEXT = "< Exit"

EXIT_TEXT_X = 8
EXIT_TEXT_Y = 12

STATUS_TEXT_X = 100
STATUS_TEXT_Y = 20
STATUS_TEXT_SCALE = 1.5

# =============================================================================
# Display Colors
# =============================================================================

COLOR_UI = image.COLOR_WHITE
COLOR_DETECTION = image.COLOR_RED
COLOR_STATUS_ON = image.COLOR_GREEN
COLOR_STATUS_OFF = image.COLOR_RED