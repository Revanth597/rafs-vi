# Models

This directory contains the object detection models, deployment assets, and label definitions used by **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)**.

RAFS-VI employs a pretrained **YOLOv11 Nano** object detection model optimized for the **Sipeed MaixCam** platform. The embedded firmware uses the model to perform real-time object detection, while distance estimation and audio feedback are implemented independently by the RAFS-VI perception pipeline.

---

# Directory Structure

```text
models/
│
├── archives/
│   ├── cvimodels/
│   └── mud/
│
├── labels.txt
├── yolo11n.mud
├── yolo11n_320x224_int8.cvimodel
└── README.md
```

---

# Model Overview

The deployed model is based on **YOLOv11 Nano**, a lightweight one-stage object detector designed for resource-constrained embedded AI platforms.

The model performs:

- Real-time object detection
- Bounding-box localization
- Object classification

The resulting detections are processed by the RAFS-VI firmware to estimate object distance, apply decision logic, and generate spoken feedback.

---

# Deployment Files

## yolo11n_320x224_int8.cvimodel

This file contains the compiled INT8 inference model executed by the Neural Processing Unit (NPU) on the Sipeed MaixCam.

### Characteristics

- INT8 quantized
- Optimized for the SG2002 platform
- Low memory footprint
- Low power consumption
- Real-time embedded inference

---

## yolo11n.mud

The `.mud` file is the deployment package used by the MaixPy runtime.

It contains the information required to initialize the object detection pipeline, including:

- Model configuration
- Runtime metadata
- Associated CVI model
- Deployment parameters

The embedded firmware loads this file during system initialization.

---

# Archived Models

The `archives/` directory contains additional deployment packages and intermediate model variants generated during development.

These files are retained for documentation, comparison, and future experimentation, but are **not used by the final deployed prototype**.

---

# Object Classes

The deployed model supports all **80 Microsoft COCO object classes**.

The complete class definitions are provided in:

```text
labels.txt
```

The firmware uses these labels to associate detected objects with the corresponding prerecorded audio prompts whenever available.

---

# Runtime Pipeline

The object detection pipeline is illustrated below.

```text
RGB Camera
      │
      ▼
YOLOv11 Nano
      │
      ▼
Bounding Boxes
      │
      ▼
Object Classification
      │
      ▼
Distance Estimation
      │
      ▼
Decision Logic
      │
      ▼
Audio Feedback
```

The YOLOv11 model is responsible solely for object localization and classification. Distance estimation, filtering, and spoken feedback are implemented separately by the RAFS-VI firmware.

---

# Model Source

The deployed YOLOv11 Nano model is based on the pretrained model distributed through the **MaixHub** ecosystem and compiled for execution on the Sipeed MaixCam platform.

The RAFS-VI project builds upon this pretrained detector by integrating:

- Embedded object detection
- Monocular distance estimation
- Experimental calibration methodology
- Wearable hardware integration
- Offline speech-based user feedback

The pretrained YOLOv11 model itself was **not retrained or modified** as part of this project.

---

# Notes

- All inference is performed locally on the embedded platform.
- The deployed model supports all 80 Microsoft COCO object classes.
- No cloud-based inference or internet connectivity is required during operation.
- Spoken feedback is generated only for object classes with corresponding prerecorded audio prompts.
- Additional audio prompts can be added independently without modifying the deployed object detection model.