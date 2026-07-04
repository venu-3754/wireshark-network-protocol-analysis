# DNS Packet Analysis

## Objective

Capture and analyze DNS queries and responses using Wireshark.

## Environment

- OS: Windows 11
- Tool: Wireshark 4.6
- Protocol: DNS

## Filters Used

dns

## Observations

- DNS queries were captured successfully.
- DNS response packets contained resolved IPv4 addresses.
- Transaction IDs matched between requests and responses.
- Domain names were translated into IP addresses before HTTP communication.

## Security Impact

DNS traffic reveals the domains visited by users.
Attackers can monitor DNS traffic to understand browsing behavior or perform DNS spoofing attacks.

## Recommendation

Use DNSSEC where applicable and monitor DNS traffic for suspicious domains.