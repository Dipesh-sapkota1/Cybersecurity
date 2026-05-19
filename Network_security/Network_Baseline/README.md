# Network Traffic Baseline Report

> **Analyst:** Dipesh Sapkota &nbsp;|&nbsp; **Date:** 2026-03-25 &nbsp;|&nbsp; **Interface:** eth0 (Ethernet) &nbsp;|&nbsp; **Tool:** Wireshark 4.6.4

A 15-minute passive packet capture and full traffic baseline analysis of a home network. 253,126 packets captured, analyzed for protocol breakdown, top endpoints, unencrypted traffic, DNS behavior, TCP anomalies, and traffic volume patterns.

---

## Key Findings

| # | Severity | Finding |
|---|----------|---------|
| 1 | 🟢 Low | All observed traffic was TLS/QUIC encrypted — no plaintext HTTP, Telnet, or FTP detected |
| 2 | 🟡 Medium | High-volume QUIC traffic spikes at ~120s and ~840s — correlated with user browsing activity |
| 3 | 🟡 Medium | Traffic to DDoS-Guard LTD (Russian Federation) observed — consistent with CDN use but worth monitoring |
| 4 | 🟢 Low | 50 TCP retransmissions out of 253,126 packets (~0.019%) — network stability is healthy |
| 5 | 🟢 Low | mDNS/SSDP discovery traffic reveals local IoT devices (Chromecast, Xiaomi, Android) |

---

## Capture Summary

| Field | Value |
|-------|-------|
| Analyst | Dipesh Sapkota |
| Date | 2026-03-25 |
| Duration | 15 minutes |
| Interface | eth0 |
| Capture File | `baseline.pcap` (excluded — see note below) |
| Total Packets | 253,126 |
| Wireshark Version | 4.6.4 |
| Local IP | 192.168.1.100 |
| Gateway | 192.168.1.254 |
| DNS Resolver | 100.127.255.165 |

> **Note:** The raw `.pcap` file is excluded from this repo due to file size.
> To reproduce the capture: `tshark -i eth0 -a duration:900 -w baseline.pcap`

---

## Top 5 Source IPs

| Rank | IP Address | Packets | Organisation | Notes |
|------|------------|---------|--------------|-------|
| 1 | 192.168.1.100 | 16,208 | Internal | Primary workstation — initiated all DNS queries and TCP/HTTPS sessions |
| 2 | 199.232.211.52 | 51,774 | Fastly, Inc (US) | High-volume CDN traffic — majority TCP ACKs indicating inbound content delivery |
| 3 | 95.129.232.112 | 13,234 | DDoS-Guard LTD (RU) | HTTPS traffic via reverse proxy CDN — behavior consistent with content delivery |
| 4 | 216.150.1.1 | 1,573 | Vercel, Inc | Frontend cloud platform — normal TLS handshake and data transfer |
| 5 | 104.21.9.123 | 1,506 | Cloudflare, Inc | HTTPS via CDN/reverse proxy — standard outbound browsing traffic |

---

## Top 5 Destination IPs

| Rank | IP Address | Packets | Organisation | Country | Notes |
|------|------------|---------|--------------|---------|-------|
| 1 | 192.168.1.100 | 16,208 | Internal | — | Primary workstation |
| 2 | 199.232.211.52 | 21,640 | Fastly, Inc | United States | CDN — inbound content delivery |
| 3 | 95.129.232.112 | 17,469 | DDoS-Guard LTD | Russian Federation | CDN reverse proxy — monitor periodically |
| 4 | 69.57.172.138 | 654 | WHG Hosting Services Ltd | India | Nginx web server — normal HTTPS browsing |
| 5 | 185.199.108.154 | 500 | Fastly, Inc | United States | CDN — standard web content delivery |

---

## Protocols Observed

| Protocol | % of Traffic | Encrypted | Description |
|----------|-------------|-----------|-------------|
| TCP | ~20.8% | — | Transport layer — connection management |
| TLS | ~2.7% | ✅ Yes | Encrypted HTTPS traffic |
| UDP | ~1.5% | — | Connectionless transport (QUIC base) |
| ICMP | ~0.5% | ❌ No | Ping / diagnostics |
| ARP | ~0.2% | ❌ No | Local address mapping — ~2,500 broadcasts |
| mDNS | ~0.1% | ❌ No | Local device discovery (Chromecast, Xiaomi, Android) |
| DNS | ~0.0% | ⚠️ Partial | Name resolution — 10 unique domains queried |
| HTTP | 0% | ❌ No | No unencrypted web traffic detected ✅ |
| SSDP | 0% | ❌ No | UPnP device discovery — M-SEARCH requests observed |

---

## Encryption Ratio

| Category | Packet Count | % of Total |
|----------|-------------|------------|
| Encrypted (TLS) | 16,568 | 100% |
| Unencrypted | 0 | 0% |

All observed application-layer traffic was encrypted. No plaintext HTTP, Telnet, or FTP sessions were detected during the capture window.

---

## Top DNS Queries

DNS resolver: `100.127.255.165`

| Rank | Domain | Queries | Category |
|------|--------|---------|----------|
| 1 | kali | 15 | Internal hostname |
| 2 | main.vscode-cdn.net | 12 | Software / CDN |
| 3 | chrome.cloudflare-dns.com | 10 | DNS-over-HTTPS |
| 4 | mobile.events.data.microsoft.com | 3 | Telemetry |
| 5 | westus-0.in.applicationinsights.azure.com | 2 | Cloud Monitoring |
| 6 | onedscolprdaus01.australiasoutheast.cloudapp.azure.com | 2 | Cloud Infrastructure |
| 7–10 | t-msedge.net CDN nodes | 1 each | Microsoft Edge CDN |

No suspicious or unexpected domains observed — all queries align with normal developer workstation activity (VS Code, Chrome, Microsoft telemetry).

---

## TCP Analysis

**Handshake traced:** `192.168.1.100` → `198.185.159.144` on port 443
- SYN → SYN-ACK → ACK confirmed — successful three-way handshake
- Filter used: `tcp.flags.syn == 1 and tcp.flags.ack == 0`

**Retransmissions:** 50 out of 253,126 packets (~0.019%) — within normal range, indicating a stable network.

---

## Traffic Volume Timeline

| Window | Packets/min | Activity |
|--------|-------------|----------|
| 0:00 – 1:00 | ~16,250 | TCP RST/ACK at ~60s — closed HTTPS session |
| 1:00 – 5:00 | ~31,980 | QUIC spike at ~120s from router to workstation |
| 5:00 – 10:00 | ~2,870 | Traffic subsides — continued QUIC session activity |
| 10:00 – 15:00 | ~48,820 | Large QUIC spike at ~840s — high-bandwidth encrypted burst |

Spikes at ~120s and ~840s were correlated with intentional user activity (loading multiple web pages) and do not indicate malicious behavior.

---

## Wireshark Filters Used

| Filter | Purpose | Result |
|--------|---------|--------|
| `http` | Detect unencrypted web traffic | 0 packets ✅ |
| `telnet` | Flag plaintext remote login | 0 packets ✅ |
| `ftp` | Flag plaintext file transfers | 0 packets ✅ |
| `dns` | Inspect name resolution | Queries visible |
| `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Isolate TCP SYN packets | Handshake traced |
| `tcp.analysis.retransmission` | Find retransmitted packets | 50 packets |
| `eth.dst == ff:ff:ff:ff:ff:ff` | Show broadcast traffic | ARP/mDNS observed |
| `!(arp or dns or icmp)` | Filter background noise | Used during analysis |

---

## Screenshots

| Screenshot | Description |
|------------|-------------|
| `screenshots/protocol-hierarchy.png` | Full protocol hierarchy tree |
| `screenshots/top-src.png` | Top source IPs — Statistics → Endpoints |
| `screenshots/top-dst.png` | Top destination IPs |
| `screenshots/http-filter.png` | Result of `http` display filter (0 packets) |
| `screenshots/telnet-filter.png` | Result of `telnet` display filter (0 packets) |
| `screenshots/dns-top.png` | Top DNS queries |
| `screenshots/tcp-syn.png` | TCP SYN packet filter result |
| `screenshots/io-graph.png` | I/O traffic volume — 15-minute timeline |

---

## Repository Structure

```
network-baseline/
│
├── README.md
├── .gitignore                        ← excludes *.pcap
│
├── report/
│   └── network_baseline_report.md   ← full analyst report
│
└── screenshots/
    ├── protocol-hierarchy.png
    ├── top-src.png
    ├── top-dst.png
    ├── http-filter.png
    ├── telnet-filter.png
    ├── dns-top.png
    ├── tcp-syn.png
    └── io-graph.png
```

---

## Reproducing the Capture

```bash
# List available interfaces
tshark -D

# Capture 15 minutes on eth0
tshark -i eth0 -a duration:900 -w baseline.pcap

# Top source IPs
tshark -r baseline.pcap -T fields -e ip.src \
  | sort | uniq -c | sort -rn | head 10

# Top destination IPs
tshark -r baseline.pcap -T fields -e ip.dst \
  | sort | uniq -c | sort -rn | head 10

# Protocol hierarchy
tshark -r baseline.pcap -q -z io,phs

# Top DNS queries
tshark -r baseline.pcap -Y "dns.flags.response == 0" \
  -T fields -e dns.qry.name | sort | uniq -c | sort -rn | head 20

# Encryption check
tshark -r baseline.pcap -Y "tls" | wc -l
tshark -r baseline.pcap -Y "http" | wc -l

# TCP retransmissions
tshark -r baseline.pcap -Y "tcp.analysis.retransmission" | wc -l

# Broadcast traffic
tshark -r baseline.pcap -Y "eth.dst == ff:ff:ff:ff:ff:ff" | wc -l
```

---

## References

- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [tshark CLI Documentation](https://www.wireshark.org/docs/man-pages/tshark.html)
- [ipinfo.io — IP Geolocation & Org Lookup](https://ipinfo.io)
- [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)

---

*Part of a hands-on network security learning series — Network Traffic Baseline Capstone.*
