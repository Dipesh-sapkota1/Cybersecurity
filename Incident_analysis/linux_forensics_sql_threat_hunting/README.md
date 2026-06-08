# Linux Forensics & SQL Threat Hunting

**NovaStar Logistics — Confirmed Security Breach Investigation**

[![Domain](https://img.shields.io/badge/Domain-Incident%20Analysis-b08800?style=for-the-badge&labelColor=b08800&color=0d1117)](.)
[![MITRE](https://img.shields.io/badge/MITRE%20ATT%26CK-5%20Techniques-da3633?style=for-the-badge&labelColor=da3633&color=0d1117)](https://attack.mitre.org/)
[![NIST](https://img.shields.io/badge/NIST%20SP%20800--61-Applied-8957e5?style=for-the-badge&labelColor=8957e5&color=0d1117)](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
[![Status](https://img.shields.io/badge/Status-Complete-238636?style=for-the-badge&labelColor=238636&color=0d1117)](.)

---

## What This Project Is

A hands-on forensic investigation simulating a real-world Linux server compromise. Working from raw `auth.log` entries and a web application database, I reconstructed the full attack from initial brute-force through data exfiltration — the same workflow a SOC analyst or DFIR responder would follow.

**The scenario:** NovaStar Logistics' production server `prod-web-01` was compromised on January 15, 2024. My task was to determine what happened, how, and what to do about it — using only the logs and SQL data.

---

## What I Did

**Part 1 — Linux Log Analysis (`auth.log`)**
- Parsed SSH authentication logs to identify brute-force sources and attempt counts
- Confirmed breach: identified successful unauthorized login and the exact timestamp
- Detected persistence mechanism: backdoor account creation 24 minutes post-breach
- Reconstructed a complete attack timeline from first probe to exfiltration

**Part 2 — SQL Threat Hunting**
- Queried `user_sessions` to isolate attacker activity during the breach window
- Queried `data_exports` to quantify exfiltration volume (83.6 MB across 2 files)
- Queried `access_logs` to identify and classify 5 SQL injection payloads from 2 IPs

**Part 3 — Incident Report**
- Documented root cause, evidence, containment commands, and long-term remediation
- Mapped attacker actions to MITRE ATT&CK techniques
- Produced actionable containment steps executable within 30 minutes

---

## Key Findings

| Finding | Detail |
|---|---|
| **Initial access vector** | SSH brute-force — 112 attempts in 4 minutes, no lockout in place |
| **Compromised account** | `deploy` service account — password auth enabled, no rate-limit protection |
| **Breach time** | Jan 15, 02:54:12 AM — 4 minutes after attack began |
| **Persistence** | Backdoor account `sysbackup` (UID=1002) created at 03:18:44 AM |
| **Data exfiltrated** | 83.6 MB — `backup_users_ALL.tar.gz` + `db_dump_full.sql.gz` |
| **SQL injection** | 5 payloads across 2 IPs: auth bypass, UNION SELECT, time-based blind, DROP TABLE |
| **Second attacker IP** | `91.108.4.200` — targeted `root` via SSH and `/admin/` endpoint (both blocked) |

---

## MITRE ATT&CK Coverage

| Technique | ID | Evidence |
|---|---|---|
| Brute Force: Password Guessing | T1110.001 | 112 failed SSH attempts from `185.220.101.47` |
| Valid Accounts | T1078 | `deploy` account compromised via password |
| Unix Shell | T1059.004 | Interactive session confirmed (UID=0 session open) |
| Exploit Public-Facing Application | T1190 | sqlmap payloads against web app login/search/products |
| Create Account: Local Account | T1136.001 | `sysbackup` backdoor account — `useradd[3301]` log entry |
| Data from Local System | T1005 | `file_download` session at 03:14:22 AM |
| Exfiltration Over Alternative Protocol | T1048 | 83.6 MB transferred to external IP over SSH session |

---

## Files in This Directory

```
linux_forensics_sql_threat_hunting/
├── README.md                                    ← You are here
└── linux-forensics-sql-threat-hunting.md        ← Full investigation report
```

---

## Skills Demonstrated

- Linux log forensics (`grep`, `awk`, `sort`, `uniq` for log parsing)
- SQL threat hunting (`WHERE`, `GROUP BY`, `HAVING`, `LIKE` for anomaly detection)
- Attack timeline reconstruction
- MITRE ATT&CK technique mapping
- Incident response: containment, evidence preservation, remediation
- Forensic bash scripting (one-liner for IP extraction and reverse DNS)
