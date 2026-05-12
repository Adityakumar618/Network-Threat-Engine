# 🚀 Live Network Defense System

This project offers a **Live Network Defense System** fueled by anomaly detection and real-time alerting. It includes simulated attacks, a live network sniffer, and a powerful analytics engine for detecting suspicious activity on your network.

---

## 📜 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
4. [Dataset and Model](#dataset-and-model)
5. [Simulated Attack](#simulated-attack)
6. [Live Traffic Sniffer](#live-traffic-sniffer)
7. [Installation](#installation)
8. [Contributing](#contributing)
9. [License](#license)

---

## 🧩 Introduction

The **Live Network Defense System** is an AI-powered Intrusion Detection System (IDS) designed to monitor traffic in real time, raise alerts for anomalies, and log each connection. Its primary components include:

1. `simulate_attack.py`: A script that simulates malware-like behavior to test the sniffer system.
2. `live_sniffer.py`: A script featuring AI-powered, real-time packet monitoring and anomaly detection.
3. `live_traffic.csv`: A continuously updated CSV log of traffic, including scores and statuses.

---

## 🌟 Features

- **AI-Powered Anomaly Detection**: Leverages a pre-trained Scikit-learn model to detect traffic anomalies.
- **Real-Time Alerts**: Colored terminal output for immediate feedback.
  - 🔴 Alerts for anomalies (`🚨 ALERT`)  
  - 🟢 Safe traffic (`OK`)
- **Simulated Malware Behavior**: Simulates anomalous connection attempts to test the system's effectiveness.
- **CSV Traffic Logs**: Captures traffic data for offline analysis or dashboard integration.
- **Extensible and Modular**: Built to integrate with larger network monitoring or defense systems.

---

## 🔧 Usage

### 1️⃣ Simulate Traffic Using `simulate_attack.py`
Run the attack simulation script:
```bash
python simulate_attack.py
```

This script simulates suspicious connection attempts to predefined malicious ports (e.g., 4444, 1337, 666) on Google's DNS server.

### 2️⃣ Start the Live Sniffer Using `live_sniffer.py`
```bash
sudo python live_sniffer.py
```
- Requires elevated privileges (`sudo`) to capture network packets.
- Monitors incoming and outgoing traffic in real time.
- Logs traffic in `live_traffic.csv`.

### 3️⃣ Analyze Traffic Logs
The file `live_traffic.csv` contains:
- `Time` of capture
- `Source` IP
- `Destination` IP
- `Port` used
- `Score` (anomaly level)
- `Status` (e.g., `OK`, `ALERT`)

---

## 📂 Dataset and Model

This project uses a pre-trained **lightweight anomaly model** trained on **CIC-IDS2017** features. The following artifacts should be in your working directory:

- **`ids_model_lite.pkl`**: Includes the pre-trained Scikit-learn model and feature scaler.
- **Key Model Features**:
    - `Destination Port`
    - `Total Length of Fwd Packets`
    - `FIN Flag Count`
    - `SYN Flag Count`
    
---

## 🧪 Simulated Attack

`simulate_attack.py` targets suspicious ports commonly used by malware (like Metasploit payloads):
- IP: `8.8.8.8` (Google's DNS Server)
- Ports: `4444`, `1337`, `31337`, `666`

> **Note**: This script is for simulation purposes only and should not be used maliciously.

---

## 🛡️ Live Traffic Sniffer

`live_sniffer.py` listens to packets entering/leaving the network, evaluates them using the anomaly detection model, and writes results to `live_traffic.csv`:

#### Feature Pipeline:
1. **Extract Features**: Protocol type, port, flags, etc.
2. **Scale Features**: Adjust raw metrics using the pre-trained scaler.
3. **Model Prediction**: Measure anomaly scores above a threshold (`-0.11`).
4. **Log Data**: Store packet details and prediction status in CSV.

#### Alerts:
- **Anomalous Traffic**: Displays a 🚨 `ALERT` in red.
- **Normal Traffic**: Displays `OK` in green.

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/live-network-defense.git
cd live-network-defense
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. [Optional] Test with Scapy and elevate privileges:
```bash
sudo pip install scapy
```

4. Run the scripts:
   - Simulate traffic:
   ```bash
   python simulate_attack.py
   ```
   - Start live detection:
   ```bash
   sudo python live_sniffer.py
   ```

---

## 👩‍💻 Contributing

Your contributions are welcome! Feel free to:
- Report bugs
- Submit feature requests
- Optimize the AI model
- Enhance packet analysis features

1. Fork the repository:
   ```bash
   git clone https://github.com/your-username/live-network-defense.git
   ```
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**, allowing commercial use, modification, distribution, and private use. 

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Using software to intercept or manipulate network traffic is subject to **legal and ethical guidelines**. Always use this system on networks you own or have explicit permission to test.

---

_Optimized for cybersecurity professionals, AI researchers, and network enthusiasts._
