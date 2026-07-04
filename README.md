# 🦈 Wireshark Network Protocol Analysis

![Wireshark](https://img.shields.io/badge/Wireshark-4.6-blue)
![Windows](https://img.shields.io/badge/OS-Windows%2011-success)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# Project Overview

This project demonstrates practical **network traffic analysis** using **Wireshark** by capturing and analyzing multiple network protocols in a controlled lab environment.

The objective is to understand how common network protocols communicate, inspect packet-level communication, identify insecure transmissions, and document security findings through real packet captures.

The project includes practical analysis of:

- HTTP
- HTTP Credential Capture
- DNS
- TCP Three-Way Handshake
- ARP

---

# Architecture

<p align="center">
<img src="architecture-diagram.png" width="900">
</p>

---

# Project Workflow

```
Browser / Command Prompt
            │
            ▼
     Generate Network Traffic
            │
            ▼
      Wireshark Capture
            │
            ▼
 Packet Filtering & Analysis
            │
            ▼
 Security Findings
            │
            ▼
 Documentation & Report
```

---

# Repository Structure

```
wireshark-network-protocol-analysis
│
├── analysis
│   ├── arp-analysis.md
│   ├── dns-analysis.md
│   ├── http-analysis.md
│   ├── http-credential-analysis.md
│   └── tcp-handshake.md
│
├── captures
│   ├── arp-analysis.pcapng
│   ├── dns-analysis.pcapng
│   ├── http-analysis.pcapng
│   ├── http-credential-analysis.pcapng
│   └── tcp-handshake-analysis.pcapng
│
├── http-login-demo
│
├── reports
│   ├── executive-summary.md
│   ├── findings.md
│   ├── recommendations.md
│   └── final-report.md
│
├── screenshots
│   ├── arp
│   ├── dns
│   ├── http
│   ├── http-credentials
│   └── tcp
│
├── architecture
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# Objectives

- Capture live network traffic.
- Analyze HTTP communication.
- Demonstrate plaintext credential exposure.
- Understand DNS resolution.
- Analyze TCP connection establishment.
- Investigate ARP communication.
- Learn Wireshark packet filtering.
- Document packet-level security findings.

---

# Technologies Used

| Tool | Purpose |
|------|---------|
| Wireshark 4.6 | Packet Capture & Analysis |
| Python HTTP Server | HTTP Traffic Generation |
| Windows 11 | Host Operating System |
| Npcap Loopback Adapter | Localhost Packet Capture |
| Command Prompt | DNS & ARP Traffic Generation |

---

# Protocols Covered

| Protocol | Purpose | Wireshark Filter |
|----------|---------|------------------|
| HTTP | Request & Response Analysis | `http` |
| HTTP POST | Credential Capture | `http.request.method=="POST"` |
| DNS | Name Resolution | `dns` |
| TCP | Three-Way Handshake | `tcp.port==8000` |
| ARP | MAC Address Resolution | `arp` |

---

# Skills Demonstrated

### Network Protocol Analysis
- HTTP
- DNS
- TCP
- ARP

### Packet Analysis
- Packet Capture
- Packet Inspection
- Packet Filtering
- Protocol Decoding
- Follow HTTP Stream

### Security Analysis
- HTTP Credential Inspection
- Plaintext Traffic Analysis
- Network Traffic Investigation
- Packet-Level Troubleshooting

### Tools
- Wireshark 4.6
- Npcap Loopback Adapter
- Python HTTP Server
- Windows Command Prompt

### Documentation
- Technical Reporting
- Security Findings Documentation
- Packet Capture Documentation

---

# HTTP Packet Analysis

HTTP traffic was generated using a local Python HTTP server and captured using Wireshark.

### Display Filter

```text
http
```

### HTTP GET Request

<img src="screenshots/http/01-http-get-request.png" width="900">

---

### HTTP Response

<img src="screenshots/http/02-http-response.png" width="900">

The server responded with HTTP status codes such as **200 OK** and **304 Not Modified**.

---

### HTTP Stream

<img src="screenshots/http/03-http-stream.png" width="900">

The HTTP stream reconstructs the complete communication between the client and server.

---

### TCP Connection Before HTTP

<img src="screenshots/http/04-http-tcp-handshake.png" width="900">

TCP establishes a reliable connection before HTTP data is exchanged.

---

### Protocol Hierarchy

<img src="screenshots/http/05-http-protocol-hierarchy.png" width="900">

Protocol Hierarchy provides a summary of all protocols observed during packet capture.

---

### Conversations

<img src="screenshots/http/06-http-conversations.png" width="900">

The Conversations window summarizes communication between endpoints.

---

# HTTP Credential Analysis

A vulnerable HTTP login page was created to demonstrate how credentials can be exposed when transmitted without encryption.

### Login Page

<img src="screenshots/http-credentials/01-login-page.png" width="900">

---

### POST Request Filter

```text
http.request.method == "POST"
```

<img src="screenshots/http-credentials/02-post-request-filter.png" width="900">

---

### Captured HTTP POST Request

<img src="screenshots/http-credentials/03-post-request.png" width="900">

The submitted login request contains form data transmitted over HTTP.

---

### Plaintext Credentials

<img src="screenshots/http-credentials/04-plaintext-credentials.png" width="900">

The username and password are visible in plaintext because HTTP does not provide encryption.

---

### Follow HTTP Stream

<img src="screenshots/http-credentials/05-follow-http-stream.png" width="900">

Following the HTTP stream reconstructs the complete communication, demonstrating why sensitive credentials should never be transmitted over unencrypted HTTP.

---

# DNS Packet Analysis

DNS traffic was generated using **nslookup** and analyzed using Wireshark.

### Display Filter

```text
dns
```

### DNS Query

<img src="screenshots/dns/02-dns-query.png" width="900">

---

### DNS Response

<img src="screenshots/dns/03-dns-response.png" width="900">

---

### Name Resolution

<img src="screenshots/dns/04-dns-name-resolution.png" width="900">

The DNS response resolves a domain name into its corresponding IP address.

---

# TCP Three-Way Handshake

TCP establishes a reliable connection before application-layer communication begins.

### Display Filter

```text
tcp.port == 8000
```

### TCP FILTER

<img src="screenshots/tcp/01-tcp-filter.png" width="900">

---

### TCP SYN

<img src="screenshots/tcp/02-tcp-syn.png" width="900">

---

### TCP SYN-ACK

<img src="screenshots/tcp/03-tcp-syn-ack.png" width="900">

---

### TCP ACK

<img src="screenshots/tcp/04-tcp-ack.png" width="900">

---

### Follow TCP Three-Way-Handshake

<img src="screenshots/tcp/05-tcp-three-way-handshake.png" width="900">

---

# ARP Packet Analysis

ARP traffic was analyzed to observe how IP addresses are mapped to MAC addresses on the local network.

### Display Filter

```text
arp
```

### ARP Request

<img src="screenshots/arp/01-arp-request.png" width="900">

---

### ARP Reply

<img src="screenshots/arp/02-arp-reply.png" width="900">

---

### ARP Packet Details

<img src="screenshots/arp/03-arp-details.png" width="900">

---

### ARP Display Filter

<img src="screenshots/arp/04-arp-filter.png" width="900">

---

# Security Findings

| Finding | Risk Level | Description |
|---------|------------|-------------|
| HTTP traffic is transmitted in plaintext | High | HTTP requests and responses can be inspected by anyone with network visibility. |
| Credentials exposed over HTTP | Critical | Username and password submitted via HTTP POST requests are visible in packet captures. |
| DNS queries are unencrypted | Medium | Domain lookups can reveal browsing activity and infrastructure information. |
| ARP protocol has no authentication | Medium | ARP spoofing attacks are possible on local networks. |
| TCP provides reliability but not confidentiality | Low | TCP ensures delivery but does not encrypt transmitted data. |

---

# Recommendations

- Replace HTTP with HTTPS whenever credentials or sensitive data are transmitted.
- Enable TLS encryption for web services.
- Implement secure authentication mechanisms.
- Monitor network traffic for suspicious ARP activity.
- Use DNS over HTTPS (DoH) or DNS over TLS (DoT) where possible.
- Regularly inspect packet captures during security investigations.
- Disable insecure legacy protocols such as Telnet.
- Use SSH instead of Telnet for remote administration.

---

# Learning Outcomes

Through this project I gained practical experience in:

- Capturing live network traffic using Wireshark.
- Applying protocol-specific display filters.
- Reconstructing HTTP communications.
- Inspecting plaintext credential transmission.
- Understanding DNS name resolution.
- Analyzing TCP connection establishment.
- Investigating ARP request and reply packets.
- Documenting packet-level security observations.

---

# How to Reproduce

## Clone Repository

```bash
git clone https://github.com/venu-3754/wireshark-network-protocol-analysis.git
```

---

## Launch Local HTTP Server

```bash
cd http-login-demo
python server.py
```

---

## Start Wireshark

Select:

```
Npcap Loopback Adapter
```

---

## Capture Traffic

Generate the following traffic:

- Visit the local HTTP website
- Submit login credentials
- Perform DNS lookups
- Generate TCP traffic
- Capture ARP requests

---

## Apply Filters

```
http
```

```
http.request.method=="POST"
```

```
dns
```

```
arp
```

```
tcp.port==8000
```

---

# References

- Wireshark Official Documentation
- Npcap Documentation
- RFC 791 (IP)
- RFC 793 (TCP)
- RFC 826 (ARP)
- RFC 1035 (DNS)
- RFC 9110 (HTTP)

---

# Future Improvements

- HTTPS TLS Packet Analysis
- SSH Packet Analysis
- FTP Protocol Analysis
- DHCP Packet Analysis
- ICMP Packet Analysis
- IPv6 Traffic Analysis
- Network Forensics Case Study
- Malware Traffic Investigation

---

# Author

**SONGA VENUGOPAL**

Cybersecurity Undergraduate

Focused on:

- Network Security
- SOC Operations
- Digital Forensics
- Incident Response
- Threat Detection

GitHub:
https://github.com/venu-3754

---

## License

This project is released under the MIT License.

---

⭐ If you found this project useful, consider starring the repository.
