# HTTP Packet Analysis

## Objective

Capture and analyze HTTP communication using Wireshark.

## Environment

- OS: Windows 11
- Tool: Wireshark 4.6
- Protocol: HTTP
- Server: Python HTTP Server
- Capture Interface: Npcap Loopback Adapter

## Filters Used

http

tcp.port == 8000

## Observations

- HTTP GET requests were captured successfully.
- HTTP responses (200 OK / 304 Not Modified) were observed.
- TCP three-way handshake completed before HTTP communication.
- Traffic was transmitted in plaintext.
- Request and response headers were visible.

## Security Impact

HTTP does not encrypt traffic.
An attacker with network visibility can inspect requests and responses.

## Recommendation

Use HTTPS to protect confidentiality and integrity.