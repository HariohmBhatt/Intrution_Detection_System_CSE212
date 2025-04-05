# IDS Core - Network Intrusion Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)

---

## Overview

**IDS Core** is a robust, Python-based Intrusion Detection System designed to monitor network traffic and detect malicious activities in real time. Leveraging advanced machine learning techniques for threat detection, IDS Core captures and analyzes IP packets, providing immediate notifications and comprehensive logs to help secure your network against potential attacks.

---

## Key Features

- **Real-Time Analysis:** Instant capture and evaluation of network packets.
- **Machine Learning Integration:** Utilizes cutting-edge ML algorithms to differentiate between benign and malicious traffic.
- **Enhanced Ensemble Modeling:** Incorporates a stacked ensemble model that combines XGBoost, Random Forest, and an MLP classifier with Logistic Regression as the final estimator. This new logic improves detection accuracy and robustness by leveraging the strengths of each individual model.
- **Automated Alerts:** Sends immediate email notifications when threats are detected.
- **Comprehensive Logging:** Detailed records of network activity for forensic analysis and auditing.
- **Command-Line Interface (CLI):** Easy-to-use interface for quick deployment and management.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Methods](#installation-methods)
- [Dataset and Machine Learning Model](#dataset-and-machine-learning-model)
- [New Model Logic](#new-model-logic)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Future Directions](#future-directions)
- [Contact](#contact)

---

## Installation

### Prerequisites

Before installing IDS Core, ensure you have the following:

- **Python 3.6 or higher**
- **Operating System:**
  - Linux
  - Windows (with Npcap/WinPcap installed)
- **Privileges:**
  - Root on Linux
  - Administrator on Windows (required for packet sniffing)

### Installation Methods

#### From the Wheel File (Windows or Linux)

1. **Download** the wheel file (`ids_core-0.1.0-py3-none-any.whl`) from the project's [release page](#).
2. **Open Terminal/Command Prompt:** Navigate to the download directory.
3. **Install the Package:**
   ```bash
   pip install ids_core-0.1.0-py3-none-any.whl
   ```

## Dataset and Machine Learning Model

The IDS Core system utilizes a network intrusion detection dataset (e.g., KDDTest+) to train its machine learning model. The dataset undergoes preprocessing steps including:

- **Feature Selection:** Reducing the dataset to the most relevant 15 features based on mutual information.
- **Encoding:** Converting categorical variables into numeric labels.
- **Standardization:** Scaling features to improve model performance and convergence.

### What the Machine Learning Model Does

The machine learning model in IDS Core is designed to analyze network traffic data and classify it as either normal or indicative of an attack. The model achieves this through:

- **Anomaly Detection:** Leveraging advanced algorithms to identify unusual patterns in network activity that may signify a security threat.
- **Pattern Recognition:** Differentiating between benign traffic and potential intrusions by learning from historical data.
- **Robust Classification:** Employing a combination of classifiers to boost overall prediction accuracy and minimize false positives.

---

## New Model Logic

### Enhanced Ensemble Modeling

To further improve the performance of IDS Core, a new stacked ensemble model has been integrated. This model uses the following architecture:

- **Base Models:**
  - **XGBoost:** Captures complex patterns in the data using gradient boosting.
  - **Random Forest:** Offers robustness and generalization through the aggregation of multiple decision trees.
  - **MLP Classifier:** A neural network approach to capture nonlinear relationships.
- **Meta-Estimator:**
  - **Logistic Regression:** Combines the predictions from the base models to deliver the final decision, improving overall accuracy and reducing overfitting.

This ensemble approach enables IDS Core to make more robust predictions by leveraging the strengths of multiple algorithms, making it highly effective in real-world network security scenarios.

---

## Usage

1. **Start IDS Core:** Launch the IDS Core application via the command-line interface.
2. **Real-Time Monitoring:** The system begins capturing network packets and analyzing them using the integrated ML models.
3. **Alerts and Logs:** When a potential threat is detected, IDS Core immediately sends out alerts and logs detailed information for further investigation.
4. **Dashboard:** Use the web-based or CLI dashboard to view live statistics and forensic logs.

---

## Contributing

Contributions are welcome! Please see our Contributing Guidelines for details on how to get started.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Future Directions

- **Enhanced Anomaly Detection:** Incorporate deep learning techniques for more advanced anomaly detection.
- **Improved Alerting System:** Develop a more comprehensive notification system with multi-channel alerts.
- **Scalability:** Enhance system performance to handle high volumes of network traffic in real time.
- **User Interface:** Build a more user-friendly dashboard for monitoring and managing network security.

---

## Contact

For questions, suggestions, or contributions, please contact us at:

- Email: [bhatthariohm2004@gmail.com](mailto:bhatthariohm2004@gmail.com)
- GitHub: [HariohmBhatt](https://github.com/HariohmBhatt)
