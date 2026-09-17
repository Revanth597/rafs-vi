# Conference Materials — I-SMAC 2026

This directory contains the official conference presentation materials associated with the **RAFS-VI (Real-Time Assistive Framework for Situational Vision)** project.

The project was presented at the **IEEE International Conference on Smart Computing and Engineering Applications (I-SMAC 2026)**.

---

## Contents

| File | Description |
|------|-------------|
| `I-SMAC-926_Presentation.pptx` | Conference presentation covering the RAFS-VI system architecture, hardware implementation, object detection, monocular distance estimation, experimental evaluation, and future scope |
| `I-SMAC-926_Certificate.pdf` | Certificate associated with the conference presentation |
| `README.md` | Documentation for the conference materials |

> The research manuscript is maintained separately under the [`paper/`](../paper/) directory.

---

## Conference Presentation

### Title

**Design and Development of a Stand-Alone Goggle with Situational Awareness for Visually Challenged**

### Project

**RAFS-VI — Real-Time Assistive Framework for Situational Vision**

### Authors

- Parthavi N R
- Revanth A H
- Manikandan J

### Affiliation

**Department of Computer Engineering, Robotics and Internet of Things (CORI) and Electronics and Communication Engineering (ECE)**  
**PES University, Bengaluru, India**

---

## Presentation Overview

The presentation describes the development of a stand-alone assistive vision system designed to provide visually challenged users with environmental awareness through:

- Real-time object detection
- Monocular distance estimation
- On-device processing
- Audio-based feedback
- Portable hardware implementation

The system uses a **LicheeRV Nano** platform with a camera module to capture the surrounding environment and perform vision processing locally.

---

## System Highlights

### Object Detection

The system employs a **YOLOv11-based object detection model** trained using the **COCO dataset**, supporting recognition of up to **80 object classes**.

### Distance Estimation

Object distance is estimated from monocular camera information using bounding-box geometry and calibrated relationships between image measurements and ground-truth distance.

Separate calibration models are used for different distance ranges to improve the correspondence between image-space measurements and physical distance.

### Audio Feedback

Detected objects and their estimated distances are communicated to the user through an audio output interface.

Example:

```text
Person detected at 1 metre
Table detected at 0.5 metre