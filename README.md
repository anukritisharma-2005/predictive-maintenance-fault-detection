# Predictive Maintenance & Fault Detection for Electronic Circuits
## Live Dashboard

Streamlit App:
https://predictive-maintenance-fault-detection-klyhpexeptdzlxfunpdgsa.streamlit.app
## Overview

This project implements an end-to-end predictive maintenance pipeline for electronic systems using machine learning and anomaly detection techniques.

The system analyzes sensor data (voltage, current, and temperature) to:

* Detect anomalous behavior
* Predict failures before they occur
* Quantify how early faults become detectable using a novel Fault Precursor Window Predictor
* Compare unsupervised anomaly detection against supervised fault classification

The project was developed as a research-oriented predictive maintenance system inspired by anomaly detection approaches used in large-scale scientific infrastructures such as CERN's CMS detector electronics.

---

## Project Objectives

### 1. Anomaly Detection

Train an LSTM Autoencoder exclusively on normal operating conditions and identify deviations through reconstruction error.

### 2. Early Fault Detection

Introduce a Fault Precursor Window Predictor that estimates how many samples before a fault the anomaly becomes observable.

### 3. Supervised Baseline

Compare the autoencoder against an XGBoost classifier trained directly on fault labels.

### 4. Visualization

Provide an interactive Streamlit dashboard for monitoring sensor signals, anomaly trajectories, fault alerts, and model performance.

---

## Dataset

AI4I 2020 Predictive Maintenance Dataset

Original machine variables were transformed into sensor-style channels:

* Voltage
* Current
* Temperature

Additional engineered features include:

* Rolling mean
* Rolling standard deviation
* Lag features
* Frequency-domain (FFT-based) features

---

## Methodology

### Stage 1: Feature Engineering

Features generated:

* Rolling statistics
* Lag features
* FFT-based features
* Time-preserving train/test split

---

### Stage 2: LSTM Autoencoder

Architecture:

Input Sequence

→ LSTM(64)

→ LSTM(32)

→ RepeatVector

→ LSTM(32)

→ LSTM(64)

→ Dense Output

Anomaly score:

Reconstruction Error (MAE)

Threshold:

Mean + 3 × Standard Deviation

---

### Stage 3: Fault Precursor Window Predictor

For each fault event:

1. Examine reconstruction error before failure.
2. Identify earliest threshold crossing.
3. Compute lead time.

Lead Time = Fault Timestamp − First Threshold Crossing

This provides an estimate of how early a fault becomes detectable.

---

### Stage 4: XGBoost Baseline

Features:

* Engineered sensor features
* Rolling statistics
* Lag features
* FFT features

Class imbalance handled using:

scale_pos_weight

---

### Stage 5: Dashboard

Interactive Streamlit dashboard displaying:

* Sensor signals
* Reconstruction error trajectory
* Fault alerts
* Lead-time statistics
* Model comparison

---

## Results

### LSTM Autoencoder

| Metric    | Value  |
| --------- | ------ |
| Precision | 0.0314 |
| Recall    | 0.1316 |
| F1 Score  | 0.0508 |
| ROC-AUC   | 0.5346 |

---

### Fault Precursor Window Predictor

| Metric            | Value        |
| ----------------- | ------------ |
| Mean Lead Time    | 67.5 Samples |
| Median Lead Time  | 77.5 Samples |
| Maximum Lead Time | 100 Samples  |

---

### XGBoost Baseline

| Metric    | Value |
| --------- | ----- |
| Precision | 1.000 |
| Recall    | 0.949 |
| F1 Score  | 0.974 |
| ROC-AUC   | 0.989 |

---

## Key Insight

While XGBoost achieved significantly higher classification performance, the LSTM Autoencoder enabled early-warning analysis through reconstruction-error evolution.

The proposed Fault Precursor Window Predictor detected emerging failures an average of 67.5 samples before fault occurrence.

---

## CERN Relevance

The CMS experiment at CERN employs machine-learning-based anomaly detection systems for monitoring detector electronics and identifying abnormal behavior in real time.

This project explores a related concept by analyzing how anomaly scores evolve before failures occur and quantifying the available warning horizon.

The Fault Precursor Window Predictor extends traditional anomaly detection by measuring fault detectability lead time rather than providing only binary anomaly alerts.

---

## Repository Structure

```text
app.py

dashboard/

outputs/
├── metrics/
├── models/
├── plots/
├── processed/
└── scalers/
```

---

## Technologies

* Python
* TensorFlow / Keras
* XGBoost
* Scikit-Learn
* Pandas
* NumPy
* Streamlit
* Matplotlib

---

## Future Work

* Real-time sensor streaming
* Physics-informed anomaly detection
* Transformer-based time-series models
* Digital twin integration
* Deployment on embedded hardware
* Application to detector electronics and space systems

---

## Author

Anukriti Sharma

Electronics Engineering | Robotics | Machine Learning | Predictive Maintenance Research
