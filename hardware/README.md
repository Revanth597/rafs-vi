# Hardware

This directory contains the hardware documentation for **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)**.

The hardware platform was designed as a lightweight wearable assistive system capable of performing real-time object detection and monocular distance estimation entirely on-device. The design emphasizes portability, balanced weight distribution, low power consumption, and fully offline operation.

---

# Repository Structure

```text
hardware/
│
├── BOM/
│   └── bill_of_materials.pdf
│
├── diagrams/
│   ├── lipo_configuration.png
│   └── powerbank_configuration.png
│
└── README.md
```

---

# Hardware Overview

The prototype is centered around the **Sipeed MaixCam**, an embedded AI platform integrating the SG2002 processor, RGB camera, and Neural Processing Unit (NPU) required for real-time computer vision.

The hardware supports two power configurations:

- **USB Power Bank Configuration** – intended for development, testing, and laboratory evaluation.
- **Rechargeable Li-Po Battery Configuration** – designed for portable wearable deployment.

Both configurations utilize the same embedded processing pipeline and peripheral hardware.

---

# System Components

| Component | Purpose |
|-----------|---------|
| **Sipeed MaixCam (SG2002)** | Embedded AI platform executing image processing and inference |
| **Integrated RGB Camera** | Image acquisition for object detection and distance estimation |
| **Rechargeable Li-Po Battery (3.7 V)** | Portable power source |
| **TP4056 / LT4056 Charging Module** | Battery charging and protection |
| **XL6009 DC-DC Boost Converter** | Voltage regulation for system operation |
| **Earphone / Speaker** | Offline spoken feedback |
| **Push Button** | Enables or disables object detection |
| **Status LED** | Indicates the current operating state |
| **Wearable Eyeglass Frame** | Mechanical integration of the complete system |

---

# System Architecture

The hardware follows the embedded perception pipeline illustrated below.

```text
RGB Camera
     │
     ▼
Sipeed MaixCam
(Image Processing)
     │
     ▼
AI Inference
     │
     ▼
Distance Estimation
     │
     ▼
Decision Logic
     │
     ▼
Audio Output
```

The push button and status LED provide a simple user interface while operating independently of the perception pipeline.

---

# Power Configurations

## USB Power Bank

The USB power configuration was primarily used during development and experimental evaluation.

Features include:

- Stable regulated 5 V supply
- Continuous operation
- Simplified hardware setup
- No onboard charging circuitry required

Reference diagram:

```text
hardware/diagrams/powerbank_configuration.png
```

---

## Rechargeable Li-Po Battery

The portable configuration enables untethered wearable operation.

The power subsystem consists of:

- 3.7 V Li-Po battery
- TP4056 / LT4056 charging module
- XL6009 boost converter
- Regulated power supply for the embedded platform

To improve comfort, the battery is positioned along the rear section of the eyeglass frame, helping counterbalance the front-mounted processing hardware.

Reference diagram:

```text
hardware/diagrams/lipo_configuration.png
```

---

# User Interface

## Push Button

A single tactile push button controls the operating state of the wearable.

### Detection Enabled

- Camera active
- Object detection enabled
- Distance estimation enabled
- Audio feedback enabled

### Detection Disabled

- Object detection disabled
- Distance estimation halted
- Audio playback disabled

The firmware implements a simple two-state toggle mechanism without long-press or multi-click functionality.

---

## Status LED

The status LED provides a visual indication of the current operating mode.

| LED State | System Status |
|-----------|---------------|
| **ON** | Detection Enabled |
| **OFF** | Detection Disabled |

The LED is intended solely as a status indicator and is not involved in system control.

---

# Mechanical Design

The prototype integrates all electronic components into a wearable eyeglass frame.

Key design objectives include:

- Forward-facing camera aligned with the user's natural viewing direction
- Balanced weight distribution through rear-mounted battery placement
- Compact routing of interconnecting wiring
- Hands-free operation
- Passive thermal dissipation without active cooling

The resulting design provides a compact, self-contained assistive device suitable for wearable deployment.

---

# Power Consumption

Typical operating power during continuous inference and audio feedback is approximately **2–3 W**.

The system supports:

- Continuous USB-powered operation
- Portable battery-powered operation

Both configurations operate entirely offline without requiring external computing resources or network connectivity.

---

# Bill of Materials

A complete list of hardware components, specifications, and indicative costs is provided in:

```text
hardware/BOM/bill_of_materials.pdf
```

---

# Design Philosophy

The hardware architecture was developed with the following objectives:

- Self-contained embedded operation
- Low-power AI inference
- Lightweight wearable form factor
- Balanced mechanical design
- Simple user interaction
- Real-time environmental awareness
- Reliable offline operation

These principles guided both the electrical architecture and the mechanical integration of the RAFS-VI prototype.