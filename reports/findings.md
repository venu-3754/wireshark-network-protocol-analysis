# Findings

## HTTP

- HTTP traffic was captured successfully.
- HTTP requests and responses were visible in plaintext.
- Response status codes such as 200 OK and 304 Not Modified were observed.

---

## HTTP Credential Analysis

- Login credentials transmitted over HTTP were captured successfully.
- Username and password were visible in plaintext.
- No encryption was applied to the communication.

---

## DNS

- DNS queries resolved domain names into IP addresses.
- DNS request and response packets were analyzed successfully.

---

## TCP

- The TCP three-way handshake (SYN → SYN/ACK → ACK) was successfully captured.
- Reliable connection establishment was verified before HTTP communication.

---

## ARP

- ARP request and reply packets were analyzed.
- MAC address resolution between hosts was successfully observed.