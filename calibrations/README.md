# Calibration

This directory contains the complete calibration methodology used in **RAFS-VI (Real-Time Auditory Feedback System for the Visually Impaired)** for monocular distance estimation.

The calibration process establishes the relationship between an object's observed bounding-box dimensions and its known ground-truth distance. Experimental measurements were collected under controlled conditions, followed by polynomial curve fitting in MATLAB to obtain object-specific calibration models.

The resulting calibration equations were used to evaluate the relationship between image-plane measurements and real-world distance during system development.

---

# Directory Structure

```text
calibrations/
│
├── experimental_results/
│   ├── cellphone_dist_results.pdf
│   ├── chair_dist_results.pdf
│   ├── laptop_dist_results.pdf
│   ├── person_dist_results.pdf
│   ├── suitcase_dist_results.pdf
│   └── vase_dist_results.pdf
│
├── matlab/
│   ├── plots/
│   │   ├── cellphone_calibration.png
│   │   ├── chair_calibration.png
│   │   ├── laptop_calibration.png
│   │   ├── person_calibration.png
│   │   ├── suitcase_calibration.png
│   │   └── vase_calibration.png
│   │
│   ├── distance_calibration.m
│   ├── distance_calibration_equations.pdf
│   └── README.md
│
├── testbench/
│   └── tts_testbench.py
│
└── README.md
```

---

# Calibration Workflow

The complete calibration procedure is summarized below.

```text
Known Object Placement
           │
           ▼
Image Acquisition
           │
           ▼
YOLOv11 Object Detection
           │
           ▼
Bounding Box Extraction
           │
           ▼
Automated Measurement Collection
(tts_testbench.py)
           │
           ▼
Experimental Data Generation
           │
           ▼
MATLAB Analysis
           │
           ├── Statistical Evaluation
           ├── Curve Fitting
           ├── Residual Analysis
           └── Polynomial Modeling
           │
           ▼
Object-Specific Calibration Equations
```

---

# Experimental Measurements

Calibration data were collected using a custom Python testbench that repeatedly recorded object detections at predefined ground-truth distances.

For each object and measurement distance, the testbench recorded:

- Bounding-box width
- Bounding-box height
- Estimated distance
- Multiple repeated observations

The collected measurements were statistically analyzed to determine representative values, measurement variability, and fitting accuracy.

Processed experimental summaries are available in the `experimental_results/` directory.

---

# MATLAB Analysis

Distance calibration was performed using the reusable MATLAB script provided in this repository.

For each calibrated object, the script:

- Imports the experimental dataset
- Plots bounding-box width versus ground-truth distance
- Plots bounding-box height versus ground-truth distance
- Performs polynomial curve fitting
- Generates residual plots to evaluate model accuracy

The resulting calibration figures are available in `matlab/plots/`.

---

# Calibration Models

The polynomial calibration equations generated during curve fitting are provided in:

```text
matlab/distance_calibration_equations.pdf
```

Independent calibration models were generated for each object because different object geometries produce different image-plane characteristics.

Where appropriate, both width-based and height-based polynomial models are included.

---

# Calibrated Objects

Distance calibration was performed for the following object classes:

- Cellphone
- Chair
- Laptop
- Person
- Suitcase
- Vase

Each object includes:

- Experimental measurement results
- Calibration plots
- Polynomial fitting equations
- Residual analysis

---

# Measurement Testbench

Experimental measurements were automated using the custom Python testbench located at:

```text
testbench/tts_testbench.py
```

The testbench repeatedly measures detected objects at known distances, generating the datasets used for statistical analysis and curve fitting.

---

# Relationship to the Firmware

The calibration resources contained in this directory are intended for **offline analysis and model development**.

The MATLAB scripts, experimental datasets, and calibration equations document the methodology used during system development and validation. They are **not executed by the embedded firmware during runtime**, but instead serve as supporting resources for evaluating and refining the distance estimation approach.

---

# Notes

- Distance calibration is performed independently for each object class.
- The MATLAB script is reusable by replacing the experimental datasets with measurements from other objects.
- All experimental data, plots, and calibration equations are included for reproducibility.
- This directory documents the calibration methodology and supporting analysis rather than the embedded implementation itself.