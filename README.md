# Network Port & Service Scanner

A lightweight Python network scanner that utilizes raw TCP socket streams to discover open ports and active services on a target network endpoint.

## Features
- **TCP Socket Discovery:** Scans target IP addresses for active listening ports using `socket.connect_ex`.
- **Timeout Controls:** Implements non-blocking execution with 1-second timeout limits to prevent hanging connections.
- **Exception Handling:** Gracefully handles keyboard interrupts (`Ctrl+C`), DNS resolution errors, and network reachability failures.

## Usage
Run the scanner locally using Python 3:
