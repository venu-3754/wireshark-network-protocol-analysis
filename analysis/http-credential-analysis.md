# HTTP Credential Capture Analysis

## Objective

Demonstrate plaintext credential transmission over HTTP.

## Environment

- OS: Windows 11
- Tool: Wireshark
- Local HTTP Login Server

## Filters Used

http

http.request.method == "POST"

## Observations

- Username and password were transmitted in plaintext.
- HTTP POST requests exposed submitted credentials.
- Follow HTTP Stream displayed the full request body.

## Security Impact

Plain HTTP does not encrypt credentials.
Attackers with network visibility can capture usernames and passwords.

## Recommendation

Always use HTTPS with TLS encryption to protect sensitive information.