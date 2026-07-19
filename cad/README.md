# CAD Design

This directory contains the rendered CAD visualizations of the **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)** wearable prototype.

The renders illustrate the mechanical integration of the embedded vision hardware, processing electronics, power subsystem, and audio output within a compact eyeglass-based assistive device. They provide a visual representation of the prototype design and complement the hardware documentation contained elsewhere in the repository.

---

# Directory Structure

```text
cad/
│
├── renders/
│   ├── assembly.png
│   ├── front_view.png
│   ├── left_isometric.png
│   ├── multi_view.png
│   └── right_isometric.png
│
└── README.md
```

---

# Design Objectives

The wearable prototype was designed with the following goals:

- Compact eyeglass-based form factor
- Balanced weight distribution
- Integrated embedded electronics
- Forward-facing camera placement
- Accessible user interface
- Modular mechanical construction

These objectives were intended to improve portability, usability, and ease of assembly while maintaining reliable system operation.

---

# Mechanical Architecture

The CAD model integrates all primary system components into a single wearable assembly.

The prototype includes:

- Forward-facing camera module
- Embedded processing enclosure
- Rechargeable power subsystem
- Audio output device
- Mechanical support structure
- Interconnecting wiring

The overall layout was designed to provide a self-contained assistive device while minimizing obstruction to the user's natural field of view.

---

# Camera Placement

The camera is mounted at the front of the eyeglass frame, providing an unobstructed forward-facing perspective for image acquisition.

This placement closely aligns the camera with the user's natural viewing direction, supporting real-time object detection and monocular distance estimation.

---

# Embedded Electronics

The embedded processing module is positioned adjacent to the camera assembly to reduce cable routing complexity and maintain a compact mechanical layout.

The enclosure houses the embedded hardware responsible for:

- Image acquisition
- AI inference
- Distance estimation
- Audio control
- System management

---

# Power System

The rechargeable power module is positioned along the temple arm of the eyeglass frame.

This placement improves weight distribution while preserving the wearable form factor and allowing portable, self-contained operation.

---

# Audio Output

Speech feedback is delivered through an earphone positioned near the user's ear.

During operation, the embedded firmware plays prerecorded object and distance announcements corresponding to valid object detections, enabling intuitive hands-free interaction.

---

# Render Gallery

The rendered images illustrate the prototype from multiple viewpoints.

| Render | Description |
|---------|-------------|
| **assembly.png** | Complete assembled view of the wearable prototype. |
| **front_view.png** | Front view highlighting camera placement and electronics enclosure. |
| **left_isometric.png** | Left isometric perspective of the integrated mechanical design. |
| **right_isometric.png** | Right isometric perspective showing battery placement and wiring. |
| **multi_view.png** | Composite view presenting multiple perspectives of the complete assembly. |

---

# Relationship to the Hardware

This directory focuses on the **mechanical design** of the RAFS-VI prototype.

Detailed information regarding electronic components, wiring, power configurations, and the Bill of Materials is provided in the `hardware/` directory.

Together, the hardware documentation and CAD renders present both the electrical and mechanical aspects of the complete wearable system.

---

# Notes

- These renders represent the mechanical design of the RAFS-VI research prototype.
- They are intended for visualization and documentation purposes.
- Minor differences may exist between the rendered model and the fabricated prototype due to iterative hardware development.
- Functional behavior of the system is implemented by the embedded firmware and is independent of the rendered CAD model.