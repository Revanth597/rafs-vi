# Research Paper

## Overview

This directory contains the research manuscript associated with the **RAFS-VI (Real-time Assistive Framework for the Visually Impaired)** project.

The paper presents the design and development of a low-cost, stand-alone smart goggle intended to improve situational awareness for visually challenged individuals through embedded computer vision, object detection, distance estimation, and auditory feedback.

The proposed system performs processing locally on an embedded platform, eliminating the need for smartphone tethering, cloud processing, or continuous internet connectivity. :contentReference[oaicite:1]{index=1}

---

# Manuscript

**Title:**  
*Design and Development of a Stand-Alone Goggle with Situational Awareness for Visually Challenged*

**Authors:**

- Parthavi N R
- Revanth A H
- Manikandan J

**Affiliation:**  
Department of CORI and ECE,  
PES University, Bengaluru, India. :contentReference[oaicite:2]{index=2}

**Conference:**  
I-SMAC

**Manuscript ID:**  
I-SMAC-926

---

# Research Focus

The paper investigates a stand-alone wearable system designed to provide additional environmental awareness to visually challenged users.

The proposed system focuses on:

- Real-time object detection
- Object proximity estimation
- Embedded edge-AI processing
- Auditory feedback
- Stand-alone operation
- Low-cost wearable implementation

The objective is to complement conventional mobility aids by providing information about surrounding objects without requiring physical interaction with them. :contentReference[oaicite:3]{index=3}

---

# System Approach

The proposed system combines a camera-based perception pipeline with embedded processing and audio feedback.

The overall processing sequence is:

```text
Camera
   │
   ▼
Image Acquisition
   │
   ▼
Object Detection
   │
   ▼
Bounding Box Extraction
   │
   ▼
Monocular Distance Estimation
   │
   ▼
Decision / Interpretation
   │
   ▼
Auditory Feedback
```

The complete processing pipeline is designed to execute locally on the embedded platform without relying on cloud-based computation. :contentReference[oaicite:4]{index=4}

---

# Key Results

The manuscript reports that the proposed stand-alone system:

- Costs less than **$40**.
- Supports recognition of approximately **80 object classes**.
- Achieves a reported recognition time of approximately **30–35 ms**, depending on the reported measurement section.
- Performs distance estimation using experimentally derived curve-fitting models.
- Provides auditory feedback to communicate detected object information to the user.
- Operates without smartphone tethering or internet connectivity. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

The paper also evaluates the depth-estimation approach by comparing actual and predicted object distances and reports that the residual error was negligibly small for the tested application. :contentReference[oaicite:7]{index=7}

---

# Paper Structure

The manuscript is organized into the following major sections:

1. **Introduction**
2. **Related Work**
3. **Implementation and Working Mechanism**
4. **Performance Evaluation**
5. **Conclusion**
6. **References**

The paper introduces the motivation and existing solutions, describes the proposed prototype and its operation, evaluates system performance, and concludes with the contributions of the proposed stand-alone goggle. :contentReference[oaicite:8]{index=8}

---

# Repository Relationship

The research paper documents the research and engineering work represented by the rest of this repository.

```text
RAFS-VI
│
├── hardware/       Hardware design and electronics
├── cad/            Wearable mechanical design
├── models/         Machine-learning models
├── firmware/       Embedded software
├── calibrations/   Distance-estimation calibration
├── audios/         Auditory feedback resources
├── images/         Project documentation and figures
│
└── paper/          Research manuscript
```

The paper provides the academic documentation of the system, while the associated repository directories contain the implementation artifacts supporting the reported work.

---

# Manuscript File

The complete manuscript is available as:

```text
I-SMAC-926_Final_Manuscript.pdf
```

The PDF contains the complete paper, including the system description, experimental evaluation, conclusion, and references.

---

# Citation

If this work is referenced in another publication, please cite the published version of the paper when available.

### BibTeX

```bibtex
@inproceedings{parthavi2026standalone,
  title     = {Design and Development of a Stand-Alone Goggle with Situational Awareness for Visually Challenged},
  author    = {Parthavi N R and Revanth A H and Manikandan J},
  booktitle = {I-SMAC},
  year      = {2026}
}
```

> **Note:** Update the BibTeX entry with the final publication year, conference details, page numbers, DOI, and publisher information once the official proceedings record is available.

---

# Publication Status

This directory contains the final manuscript associated with the project.

The repository may continue to evolve as additional experiments, datasets, hardware revisions, and software improvements are developed. The manuscript represents the research implementation and evaluation documented at the time of submission.

---

# Authors

**Parthavi N R**  
Department of CORI and ECE  
PES University, Bengaluru, India

**Revanth A H**  
Department of CORI and ECE  
PES University, Bengaluru, India

**Manikandan J**  
Department of CORI and ECE  
PES University, Bengaluru, India