# Final Report

# Wireshark Network Protocol Analysis

---

## Project Information

| Item | Details |
|------|---------|
| Project Name | Wireshark Network Protocol Analysis |
| Analyst | Venu Gopal |
| Platform | Windows 11 |
| Tool | Wireshark 4.6 |
| Capture Driver | Npcap |
| Capture Interface | Npcap Loopback Adapter |
| Date | July 2026 |

---

# Project Objective

The objective of this project was to perform practical network traffic analysis using Wireshark by capturing, filtering, and inspecting network packets generated in a controlled lab environment.

The project demonstrates how common protocols communicate over a network and highlights potential security risks associated with unencrypted communication.

---

# Lab Environment

## Hardware

- Windows 11 Laptop
- Wi-Fi Network Interface
- Npcap Loopback Adapter

## Software

- Wireshark 4.6
- Python 3.x HTTP Server
- Google Chrome
- Command Prompt

---

# Protocols Analyzed

| Protocol | Purpose | Status |
|----------|---------|--------|
| HTTP | Web Request & Response Analysis | ✅ Completed |
| HTTP POST | Credential Capture | ✅ Completed |
| DNS | Domain Name Resolution | ✅ Completed |
| TCP | Three-Way Handshake Analysis | ✅ Completed |
| ARP | Address Resolution Analysis | ✅ Completed |

---

# Analysis Performed

## 1. HTTP Analysis

### Objective

Capture HTTP requests and responses.

### Activities

- Captured HTTP GET requests.
- Inspected HTTP response headers.
- Verified plaintext communication.
- Followed HTTP stream.

### Result

HTTP traffic was successfully captured and analyzed.

---

## 2. HTTP Credential Capture

### Objective

Demonstrate insecure credential transmission.

### Activities

- Created a local HTTP login page.
- Submitted sample credentials.
- Captured POST requests.
- Followed HTTP stream.

### Result

Username and password were visible in plaintext.

---

## 3. DNS Analysis

### Objective

Observe DNS name resolution.

### Activities

- Generated DNS queries.
- Captured DNS request packets.
- Captured DNS response packets.
- Verified resolved IP addresses.

### Result

DNS successfully translated domain names into IP addresses.

---

## 4. TCP Three-Way Handshake

### Objective

Analyze TCP connection establishment.

### Activities

- Captured SYN packet.
- Captured SYN-ACK packet.
- Captured ACK packet.
- Followed TCP conversation.

### Result

TCP connection establishment completed successfully.

---

## 5. ARP Analysis

### Objective

Analyze local network address resolution.

### Activities

- Captured ARP Request.
- Captured ARP Reply.
- Verified MAC address mapping.
- Applied ARP display filters.

### Result

ARP successfully resolved IP addresses to MAC addresses.

---

# Wireshark Filters Used

| Purpose | Display Filter |
|----------|----------------|
| HTTP | `http` |
| HTTP POST | `http.request.method=="POST"` |
| DNS | `dns` |
| TCP | `tcp.port==8000` |
| ARP | `arp` |

---

# Security Findings

| Finding | Severity |
|----------|----------|
| HTTP traffic transmitted in plaintext | High |
| Credentials visible in HTTP POST packets | Critical |
| DNS queries reveal browsing activity | Medium |
| ARP lacks authentication | Medium |
| TCP provides reliability but not encryption | Low |

---

# Security Recommendations

- Replace HTTP with HTTPS.
- Encrypt sensitive communications using TLS.
- Disable insecure legacy protocols.
- Monitor network traffic regularly.
- Use secure authentication mechanisms.
- Monitor ARP traffic for spoofing attempts.
- Implement network segmentation where appropriate.

---

# Skills Demonstrated

- Packet Capture
- Packet Inspection
- Protocol Analysis
- HTTP Analysis
- HTTP Credential Analysis
- DNS Analysis
- TCP Analysis
- ARP Analysis
- Packet Filtering
- Follow HTTP Stream
- Network Troubleshooting
- Security Documentation
- Network Forensics Fundamentals

---

# Project Deliverables

- Wireshark packet capture files (.pcapng)
- Protocol analysis reports
- Security findings
- Executive summary
- Recommendations
- Evidence screenshots
- GitHub documentation

---

# Conclusion

This project provided hands-on experience in capturing and analyzing real network traffic using Wireshark. Practical analysis of HTTP, HTTP credential transmission, DNS, TCP, and ARP protocols improved understanding of packet-level communication and common network security risks.

The project demonstrates practical skills in network traffic analysis, protocol inspection, packet filtering, security documentation, and basic network forensics, making it suitable as a cybersecurity portfolio project for SOC Analyst, Network Security, and Blue Team roles.

---

# Repository

GitHub Repository:

**https://github.com/venu-3754/wireshark-network-protocol-analysis**
