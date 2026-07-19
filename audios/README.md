# Audio Assets

This directory contains the prerecorded speech prompts used by **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)** to provide real-time auditory feedback during system operation.

The embedded firmware dynamically combines object-specific and distance-specific voice prompts to generate natural spoken feedback for detected objects. All audio playback is performed locally on the device, enabling completely offline operation without cloud-based services.

---

# Directory Structure

```text
audios/
│
├── mp3/
│   ├── distances/
│   └── objects/
│
├── wav/
│   ├── distances/
│   └── objects/
│
└── README.md
```

---

# Audio Formats

The repository includes two audio formats used during development and deployment.

## WAV

The **WAV** files are the deployed audio assets used directly by the embedded firmware during runtime. These files are optimized for playback on the MaixCam platform.

## MP3

The **MP3** files are the original speech recordings generated during development. They are retained for archival purposes and to simplify future updates or regeneration of the deployment audio.

---

# Voice Feedback System

RAFS-VI generates spoken feedback by combining two independent audio prompts:

1. Object announcement
2. Distance announcement

For