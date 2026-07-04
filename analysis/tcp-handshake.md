# TCP Three-Way Handshake Analysis

## Objective

Analyze TCP connection establishment.

## Environment

- OS: Windows 11
- Tool: Wireshark
- Protocol: TCP

## Filters Used

tcp.port == 8000

## Observations

- SYN packet initiated the connection.
- SYN-ACK acknowledged the request.
- ACK completed the TCP three-way handshake.
- HTTP communication began only after the handshake completed.

## Security Impact

Understanding TCP handshakes helps analysts investigate connection attempts, network scans, and SYN flood attacks.

## Recommendation

Monitor abnormal TCP handshake behavior and detect incomplete connections indicative of denial-of-service attacks.