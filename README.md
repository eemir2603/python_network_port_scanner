# python_network_port_scanner
A lightweight, high-performance network security tool written in Python utilizing the standard `socket` library to conduct ethical security audits and vulnerability assessments.

 Features
- Socket-Level Scanning: Directly communicates with TCP layers to accurately determine port status.
- Exception Handling: Robust management of connection timeouts, host resolution errors, and manual keyboard interruptions.
- Clean CLI Architecture: Provides a minimalist, professional terminal interface.
- Performance Tracking: Calculates and logs the exact execution duration for performance analysis.

# 🛠️ Prerequisites & Installation
No external dependencies are required. The script runs entirely on Python's standard library.

1. Clone the repository:
   git clone https://github.com/yourusername/python-port-scanner.git
   cd python-port-scanner

2. Ensure you have Python 3.x installed.

# Usage
Run the script directly from your terminal:
python port_scanner.py

 Flow of Operation:
1. Enter the target IP address or hostname.
2. Define the target range or let the script scan the standard core ports.
3. The script initializes the connection handshake and outputs open ports instantly.

# Code Architecture Summary
The core logic relies on the three pillars of Python network programming:
- `socket.socket()`: Initializes an IPv4 TCP socket connection.
- `socket.setdefaulttimeout()`: Sets a strict connection timeout limit to optimize scanning speed.
- `datetime.now()`: Tracks performance and benchmarks scanning speed.

⚠️ Disclaimer
This tool is developed strictly for **educational purposes** and **authorized ethical auditing**. Unauthorized scanning of external networks without explicit written consent is illegal. The developer assumes no liability for misuse.
