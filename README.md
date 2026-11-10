# Network Connectivity Checker Script
A python command line utility that checks TCP connectivity to specified hosts and ports.

Designed to automate basic network troubleshooting and identify unreachable services, DNS resolution failures, and connection errors

## Tools
* Python 3
* Socket: DNS resolution and TCP connectivity testing
* Time: Execution-time measurements

## Potential improvements
* Export connectivity results to CSV.
* Accept target hosts and ports through command-line arguments.
* Log connection failures with timestamps.
* Support IPv6 connectivity testing.

## Details on current limits
* Only supports IPv4 for connectivity checks
* Test TCP connections, but not UDP or ICMP
* Total check time includes DNS resolution and TCP connection establishment.
* Doesn't continuously monitor services
