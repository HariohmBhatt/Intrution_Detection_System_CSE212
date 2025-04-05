# IDS Core - Network Intrusion Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)

---

## Overview

**IDS Core** is a robust, Python-based Intrusion Detection System designed to monitor network traffic and detect malicious activities in real time. Leveraging machine learning for advanced threat detection, IDS Core captures and analyzes IP packets, providing immediate notifications and comprehensive logs to keep your network secure.

---

## Key Features

- **Real-Time Analysis:** Instant capture and evaluation of network packets.
- **Machine Learning Integration:** Utilizes ML algorithms to differentiate between benign and malicious traffic.
- **Automated Alerts:** Sends immediate email notifications when threats are detected.
- **Comprehensive Logging:** Detailed records of network activity for analysis and auditing.
- **Command-Line Interface (CLI):** Easy-to-use interface for quick deployment and management.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Methods](#installation-methods)
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
