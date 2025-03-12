# Packet Vision

## Overview
Packet Vision is a command-line tool designed for real-time network traffic monitoring and analysis. It enables users to capture network packets, save them to `.pcap` files, and analyze traffic trends. The tool is ideal for cybersecurity enthusiasts, penetration testers, and network administrators.

## Features
- Capture live packets from a specified network interface.
- Save captured packets to `.pcap` files for offline analysis.
- Visualize network traffic trends and protocol usage.
- Analyze `.pcap` files to extract insights about packet-level communication.

## Prerequisites
- Python 3.8+
- Root or administrative privileges (required for capturing network packets)
- Linux-based system (recommended for optimal performance)

## Installation
Clone the repository:
```sh
git clone https://github.com/hafizsharjeel/Packet-vision.git
cd packet-vision
```

Set up a virtual environment and install dependencies:
```sh
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
```

## Usage

### Start Packet Capture
To capture packets in real-time from a specific interface:
```sh
sudo python3 main.py --capture --interface <INTERFACE_NAME> --count <PACKET_COUNT> --output <OUTPUT_FILE>
```
Example:
```sh
sudo python3 main.py --capture --interface eth0 --count 100 --output packets.pcap
```

### Analyze Captured Packets
To analyze an existing `.pcap` file:
```sh
python3 main.py --analyze --input <PCAP_FILE>
```
Example:
```sh
python3 main.py --analyze --input packets.pcap
```

### Display Help
For a list of available commands:
```sh
python3 main.py --help
```

## Command-Line Arguments
| Argument       | Description                                       |
|---------------|-------------------------------------------------|
| `--capture`   | Enable live packet capture mode.               |
| `--analyze`   | Enable `.pcap` file analysis mode.             |
| `--interface` | Specify the network interface for live capture. |
| `--count`     | Number of packets to capture (default: 100).    |
| `--output`    | File path to save captured packets.             |
| `--input`     | File path of the `.pcap` file to analyze.       |
| `--help`      | Display the help message.                       |

## Example Workflows

### Capturing Packets
1. Identify available network interfaces:
   ```sh
   ip link show
   ```
2. Run the capture command:
   ```sh
   sudo python3 main.py --capture --interface eth0 --count 200 --output traffic.pcap
   ```
3. View the output file:
   ```sh
   ls -lh traffic.pcap
   ```

### Analyzing Packets
Use the `.pcap` file saved earlier:
```sh
python3 main.py --analyze --input traffic.pcap
```

## Development
If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch:
   ```sh
   git checkout -b feature-name
   ```
3. Submit a pull request with your changes.

## Troubleshooting
### Permission Denied
If you encounter a permission error during packet capture:
- Ensure you are running the command with `sudo`.

## How to Use Packet Vision on Windows

### Install Python and Required Libraries
Make sure you have Python 3.8 or higher installed. Install the required Python packages using:
```sh
pip install -r requirements.txt
```

### Install Npcap
Npcap is required for packet capturing on Windows. Download and install it from the official website: [Npcap](https://npcap.com). During installation, make sure to allow "WinPcap API compatibility mode."

### Find the Correct Network Interface
Open Command Prompt and run:
```sh
ipconfig
```
Look for the active adapter in the output, such as:
```
Wireless LAN adapter Wi-Fi:
   IPv4 Address. . . . . . . . . . . : 192.168.1.10
```
The interface name in this case is likely `Wi-Fi`.

### Example Commands on Windows
#### Capture Live Packets:
```sh
python main.py --capture --interface "Wi-Fi" --count 50 --output captured_packets.pcap
```
#### Analyze Packets:
```sh
python main.py --analyze --input captured_packets.pcap
```

### Missing Dependencies
If Python libraries are missing, install them with:
```sh
pip install -r requirements.txt
```

### No Network Interfaces Detected
Check your network settings and permissions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## About the Author
Hi, I’m **Hafiz Sharjeel Shakeel**, a **Cybersecurity Penetration Tester and Ethical Hacker** with a passion for creating secure tools and exploring advanced network traffic analysis techniques.
