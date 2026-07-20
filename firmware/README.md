# Firmware

This directory contains the embedded firmware developed for **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)**.

The firmware is designed for the Sipeed MaixCam platform and performs the complete perception pipeline locally, including image acquisition, object detection, monocular distance estimation, user interaction, and real-time spoken feedback. All processing is executed on-device, enabling fully offline operation without cloud services, external computation, or internet connectivity.

---

# Directory Structure

```text
firmware/
│
├── releases/
│   ├── v1.0/
│   ├── v1.1/
│   ├── v1.2/
│   ├── v1.3/
│   └── v1.4/
│
├── main.py
├── hardware.py
├── config.py
├── distance.py
├── audio_utils.py
├── ui.py
├── utils.py
│
├── CHANGELOG.md
└── README.md
```

---

# Firmware Architecture

The firmware follows a modular software architecture to improve readability, maintainability, and future extensibility.

| Module | Responsibility |
|---------|----------------|
| `main.py` | Main application loop and control logic |
| `hardware.py` | Initializes camera, display, touchscreen, audio, GPIO, and YOLO detector |
| `config.py` | Centralized firmware configuration constants |
| `distance.py` | Monocular distance estimation and formatting |
| `audio_utils.py` | Audio playback and spoken announcement handling |
| `ui.py` | Embedded user interface rendering |
| `utils.py` | Shared helper functions |

---

# Processing Pipeline

```text
Camera
   │
   ▼
YOLOv11 Inference
   │
   ▼
Bounding Box Extraction
   │
   ▼
Distance Estimation
   │
   ▼
Detection Validation
   │
   ▼
Announcement Decision
   │
   ▼
Object Audio
   │
   ▼
Distance Audio
```

---

# Responsibilities

The firmware is responsible for:

- Camera initialization
- Loading the YOLOv11 detection model
- Real-time object detection
- Bounding-box extraction
- Monocular distance estimation
- Detection filtering
- Duplicate announcement suppression
- Announcement cooldown management
- Audio playback
- User interaction
- Status indication

---

# Distance Estimation

Object distance is estimated using a calibration-based monocular vision model.

The implementation combines camera parameters with detected bounding-box width to estimate the distance between the user and surrounding objects.

Calibration methodology and experimental data are available in the `calibrations/` directory.

---

# Audio Feedback

When a valid detection is accepted:

1. The object announcement is played.
2. The corresponding distance announcement is played.

Example:

> Person... 1.5 meters.

Objects without an associated prerecorded voice prompt continue to be detected normally but are not announced.

---

# User Interface

The embedded interface consists of:

- Touchscreen exit button
- Push button to enable or disable detection
- Status LED
- Live detection overlays

---

# Design Objectives

The firmware was developed with the following objectives:

- Fully offline execution
- Real-time inference
- Modular architecture
- Maintainable source code
- Low-latency response
- Lightweight implementation
- Reliable operation

---

# Firmware Releases

Development history is documented in `CHANGELOG.md`.

Current release:

**Version 1.4**

---

# Authors

- Revanth A H
- Parthavi N R