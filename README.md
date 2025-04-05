# IDS Core - Network Intrusion Detection System

A Python-based Intrusion Detection System (IDS) that uses machine learning to detect malicious network traffic.

## Overview
`ids_core` is a Python-based Intrusion Detection System (IDS) designed to monitor network traffic for malicious activities. The system captures IP packets, analyzes them, and logs the results, providing real-time notifications when malicious packets are detected.

## Features
- Real-time packet capture and analysis
- Machine learning-based threat detection
- Automated email alerts when malicious packets are detected
- Detailed logging of network activity
- Command-line interface for easy deployment

## Installation

### Prerequisites

- Python 3.6 or higher
- Linux operating system or Windows with Npcap/WinPcap installed
- Root privileges on Linux or Administrator privileges on Windows (for packet sniffing)

### Installation Methods

#### From the wheel file (Windows or Linux)

1. Download the wheel file (`ids_core-0.1.0-py3-none-any.whl`) from the project's release page
2. Open a terminal/command prompt and navigate to the download location
3. Install the package:
   ```bash
   pip install ids_core-0.1.0-py3-none-any.whl
````

## Usage
To start the IDS, run the following command:
```
ids-core
```

## Structure
The project consists of the following main components:
- **main.py**: Entry point for the application.
- **packet_sniffer.py**: Captures network packets.
- **packet_analyzer.py**: Analyzes captured packets and classifies them.
- **notifications/email_notifier.py**: Handles email notifications for malicious packets.
- **utils/logger.py**: Provides logging functionality.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.