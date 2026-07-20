"""
Blind Assist Application

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Handles audio playback for detected objects
    and estimated distances.

Copyright (c) 2026
"""
"""
audio_utils.py

Audio playback utilities for the Blind Assist application.
"""

import os

from maix import time

from config import (
    OBJECT_AUDIO_DIR,
    DISTANCE_AUDIO_DIR,
    DEFAULT_AUDIO_VOLUME,
    AUDIO_GAP_MS,
)


def play_wav(player, file_path, volume=DEFAULT_AUDIO_VOLUME):
    """
    Play a WAV file asynchronously.

    Parameters
    ----------
    player
        Initialized Maix audio player.

    file_path : str
        Absolute path to the WAV file.

    volume : int
        Playback volume.
    """

    try:
        with open(file_path, "rb") as f:
            data = f.read()

        player.volume(volume)
        player.play(data)

    except Exception as e:
        print(f"Audio play failed: {e}")


def announce_detection(player, label, distance_label):
    """
    Play object name followed by distance.

    Behaviour is identical to the original tts4.py.

    Parameters
    ----------
    player
        Initialized audio player.

    label : str
        Detected object label.

    distance_label : str
        Formatted distance string
        (e.g. "0.8m", "2m", "2.5m").
    """

    label_path = f"{OBJECT_AUDIO_DIR}/{label}.wav"
    distance_path = f"{DISTANCE_AUDIO_DIR}/{distance_label}.wav"

    if os.path.exists(label_path):
        play_wav(player, label_path)
        time.sleep_ms(AUDIO_GAP_MS)

    if os.path.exists(distance_path):
        play_wav(player, distance_path)
    else:
        print(f"No sound file for {distance_label}")