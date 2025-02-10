# FakeDNS Tool - A Simple DNS Spoofing Utility

## Introduction

FakeDNS is a lightweight Python tool designed for ethical penetration testing and network traffic manipulation. It allows you to spoof DNS queries and redirect them to a target IP. This tool simulates a DNS hijacking scenario, useful for understanding how a network reacts under malicious conditions.

---

## Dependencies

- Python 3.x
- Scapy
- Root privileges

---

## Installation

To get started, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/YourRepo/FakeDNS.git
    cd FakeDNS
    ```

2. Install the necessary libraries:

    ```bash
    pip install scapy
    ```

---

## Usage

To run FakeDNS, you need root privileges to intercept DNS traffic.

1. Launch the tool with the following command:

    ```bash
    sudo python FakeDNS.py
    ```

2. The tool will prompt you for the following inputs:
    - The domain you wish to spoof
    - The IP address to redirect traffic to

---

## Example

Example of the tool in action:

```bash
$ sudo python FakeDNS.py
Enter the domain you want to spoof (e.g., example.com): example.com
Enter the IP address to redirect example.com to: 192.168.1.100
