# Firmware

This directory contains the embedded firmware developed for **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)**.

The firmware coordinates the complete perception pipeline, including image acquisition, object detection, monocular distance estimation, decision making, and real-time audio feedback. All processing is performed locally on the embedded platform, enabling fully offline operation without cloud services, external computation, or internet connectivity.

---

# Directory Structure

```text
firmware/
│
├── releases/
│   ├── v1.0/
│   ├── v1.1/
│   ├── v1.2/
│   └── v1.3/
│
├── CHANGELOG.md
└── README.md
```

---

# Processing Pipeline

The embedded application follows the processing pipeline illustrated below.

```text
Camera Frame
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
Detection Filtering
      │
      ▼
Decision Logic
      │
      ▼
Audio Playback
```

Each stage executes sequentially on the embedded platform, allowing the system to deliver real-time spoken feedback while maintaining low computational overhead.

---

# Responsibilities

The firmware is responsible for:

- Initializing the camera and embedded hardware
- Loading the deployed YOLOv11 model
- Performing real-time object detection
- Extracting bounding-box information
- Estimating object distance using monocular geometry
- Filtering unreliable detections
- Suppressing duplicate announcements
- Managing announcement timing
- Controlling audio playback
- Processing user input
- Managing system status indicators

---

# Distance Estimation

Object distance is estimated using a calibration-based monocular vision approach.

The runtime implementation combines bounding-box measurements with experimentally derived calibration models to estimate the distance between the user and detected objects.

The calibration methodology, datasets, and supporting analysis are documented in the `calibrations/` directory.

---

# Detection Management

To improve usability and reduce unnecessary audio feedback, several filtering stages are applied before an announcement is generated.

These include:

- Confidence thresholding
- Duplicate detection suppression
- Announcement cooldown management
- Stable detection selection

These mechanisms help reduce repetitive announcements while maintaining responsive system behavior.

---

# Audio Feedback

When a valid detection is accepted, the firmware selects the corresponding object announcement and distance announcement from the available audio assets.

If both audio prompts are available, they are played sequentially to produce natural spoken feedback.

Example:

> Person... 1.5 meters.

Objects without a corresponding prerecorded voice prompt continue to be detected normally, although no spoken announcement is generated for that object.

---

# User Interface

The wearable prototype provides a simple embedded user interface consisting of:

- Push button
- Status LED

The push button enables or disables object detection, while the status LED provides a visual indication of the current operating state.

---

# Firmware Releases

The firmware evolved through multiple development iterations during the implementation of RAFS-VI.

Each release introduces improvements in functionality, stability, and overall system performance.

A detailed development history is available in `CHANGELOG.md`.

---

# Design Objectives

The firmware was developed with the following objectives:

- Fully offline execution
- Real-time embedded inference
- Low-latency processing
- Lightweight software architecture
- Low power consumption
- Reliable operation
- Modular and maintainable code

---

# Notes

- All processing is performed on the embedded device.
- No cloud services or smartphone connectivity are required.
- Object detection, distance estimation, and audio feedback execute entirely on the MaixCam platform.
- The firmware is designed to operate as a self-contained embedded application.