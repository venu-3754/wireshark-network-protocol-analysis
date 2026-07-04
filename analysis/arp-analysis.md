# ARP Packet Analysis

## Objective 

Capture and analyze ARP requests and replies.

## Environment

- OS: Windows 11
- Tool: Wireshark
- Protocol: ARP

## Filters Used

arp

## Observations

- ARP Request packets were observed.
- ARP Reply packets mapped IP addresses to MAC addresses.
- Communication occurred before IP traffic.

## Security Impact

ARP is unauthenticated and vulnerable to ARP spoofing attacks.
Attackers can perform Man-in-the-Middle attacks by poisoning ARP caches.

## Recommendation

Use Dynamic ARP Inspection (DAI), static ARP entries where appropriate, and monitor for duplicate ARP replies.
