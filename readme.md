<div align="center">

# Cybersecurity Portfolio

**Hands-on security projects built during professional training**

[![Projects](https://img.shields.io/badge/Projects-6-0d1117?style=for-the-badge&labelColor=238636&color=0d1117)](.)
[![Domains](https://img.shields.io/badge/Domains-4-0d1117?style=for-the-badge&labelColor=1f6feb&color=0d1117)](.)
[![Framework](https://img.shields.io/badge/NIST%20SP%20800--61-Referenced-0d1117?style=for-the-badge&labelColor=8957e5&color=0d1117)](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Referenced-0d1117?style=for-the-badge&labelColor=da3633&color=0d1117)](https://attack.mitre.org/)

</div>

---

## About This Repository

This repository documents my practical cybersecurity work — audits, incident response, network analysis, and security documentation — built during my cybersecurity bootcamp and continued as independent study.

Each project is grounded in real-world frameworks (NIST, MITRE ATT&CK, CIS Controls, GDPR) and structured the way professional security teams organize their work. The goal is not just to demonstrate technical knowledge, but to show that I can produce documentation and artifacts a real security team could actually use.

> This is a living repository. New projects are added as completed. Each project directory has its own README with full context.

---

## Skills Demonstrated

| Domain | Skills |
|---|---|
| **GRC** | Security auditing, risk assessment, compliance gap analysis, control mapping (NIST CSF, PCI-DSS, GDPR), policy writing |
| **Incident Response** | Phishing IR playbook, NIST lifecycle application, RACI mapping, severity classification, evidence handling |
| **Incident Analysis** | Linux log forensics, SQL threat hunting, timeline reconstruction, root cause analysis, MITRE ATT&CK mapping |
| **Network Security** | Packet capture analysis (Wireshark), baseline documentation, protocol hierarchy, traffic analysis |
| **Documentation** | Technical writing, professional security documentation, template development |

---

## Project Index

### 🔵 GRC — Governance, Risk & Compliance

<table>
<tr>
<td width="60%">

#### [Botium Toys — Security Audit & Risk Assessment](GRC_report/botium_toys_audit_&_risk_assessment/)

A full internal security audit of Botium Toys, a fictional e-commerce company. Covers control assessment, compliance gap analysis across PCI-DSS, GDPR, and SOC 2, NIST CSF maturity reporting, risk register, and policy documentation.

**Artifacts:** Audit report · Compliance matrix · Risk register · Gap analysis · Access control policy · Password policy · Executive summary · MFA implementation plan

</td>
<td width="40%" align="center">

![GRC](https://img.shields.io/badge/-Audit-238636?style=flat-square)
![GRC](https://img.shields.io/badge/-Risk%20Assessment-238636?style=flat-square)
![GRC](https://img.shields.io/badge/-PCI--DSS-238636?style=flat-square)
![GRC](https://img.shields.io/badge/-GDPR-238636?style=flat-square)
![GRC](https://img.shields.io/badge/-NIST%20CSF-238636?style=flat-square)
![GRC](https://img.shields.io/badge/-SOC%202-238636?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

---

### 🔴 Incident Response — Playbook

<table>
<tr>
<td width="60%">

#### [Email Phishing Incident Response Playbook — NexaCore Technologies](Playbook/phishing_ir_playbook/)

A complete, operational IR playbook for a fictional mid-size fintech company. Built around NIST SP 800-61 with decision-based response flows, RACI matrix, 4-tier severity classification, tool-specific procedures, communication templates, and compliance notification requirements (GDPR, PCI-DSS).

**Artifacts:** Full playbook · Quick reference card · Incident ticket template · Notification templates · Response flow diagram · References

</td>
<td width="40%" align="center">

![IR](https://img.shields.io/badge/-NIST%20SP%20800--61-da3633?style=flat-square)
![IR](https://img.shields.io/badge/-MITRE%20T1566-da3633?style=flat-square)
![IR](https://img.shields.io/badge/-Phishing-da3633?style=flat-square)
![IR](https://img.shields.io/badge/-M365%20Defender-da3633?style=flat-square)
![IR](https://img.shields.io/badge/-CrowdStrike-da3633?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

---

### 🟡 Incident Analysis

<table>
<tr>
<td width="60%">

#### [Linux Forensics & SQL Threat Hunting — NovaStar Logistics](Incident_analysis/linux_forensics_sql_threat_hunting/)

A hands-on forensic investigation of a confirmed server breach. Working from raw `auth.log` data and a web application database, I reconstructed the full attack chain from initial brute-force through persistence establishment and data exfiltration — the same workflow a SOC analyst or DFIR responder would follow. Identified 5 MITRE ATT&CK techniques across 2 attacker IPs, quantified 83.6 MB of exfiltrated data, and produced actionable containment and remediation guidance.

**Artifacts:** Full investigation report · Attack timeline · SQL threat hunting queries · Containment procedures · MITRE ATT&CK mapping

</td>
<td width="40%" align="center">

![IA](https://img.shields.io/badge/-Linux%20Forensics-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-SQL%20Threat%20Hunting-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-MITRE%20ATT%26CK-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-Brute%20Force-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-SQL%20Injection-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-Data%20Exfiltration-b08800?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

<table>
<tr>
<td width="60%">

#### [Incident Timeline Analysis](Incident_analysis/incident_timeline/)

Structured analysis and timeline reconstruction of a security incident. Documents the sequence of attacker actions, detection gap, and response timeline in a format consistent with professional post-incident reporting.

**Artifacts:** Timeline report · Visual timeline diagram · Research references

</td>
<td width="40%" align="center">

![IA](https://img.shields.io/badge/-Timeline%20Analysis-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-Post--Incident%20Review-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-Root%20Cause%20Analysis-b08800?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

<table>
<tr>
<td width="60%">

#### [Phishing Email Analysis — sample-10.eml](Incident_analysis/phishing_analysis/)

Static forensic analysis of a real-world phishing email sourced from a public honeypot repository. The email impersonates the Microsoft account security team to create urgency and trick the recipient into clicking a malicious tracking URL. Covers full header inspection, sender infrastructure tracing, IOC extraction, and MITRE ATT&CK mapping.

**Artifacts:** Analysis report · IOC table · MITRE ATT&CK mapping · Defanged URL documentation · URL reputation screenshots (VirusTotal, Cisco Talos, BrightCloud) · Email sample (SHA256 verified)

</td>
<td width="40%" align="center">

![IA](https://img.shields.io/badge/-Phishing%20Analysis-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-Header%20Forensics-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-IOC%20Extraction-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-MITRE%20ATT%26CK-b08800?style=flat-square)
![IA](https://img.shields.io/badge/-VirusTotal-b08800?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

---

### 🟣 Network Security

<table>
<tr>
<td width="60%">

#### [Network Traffic Baseline Analysis](Network_security/Network_Baseline/)

Packet capture and analysis using Wireshark to establish a network baseline. Covers protocol hierarchy analysis, identification of top talkers, ARP/DNS/HTTP/TCP traffic filtering, and documentation of normal vs. anomalous traffic patterns.

**Artifacts:** Analysis report · Protocol hierarchy · Traffic screenshots (ARP, DNS, HTTP, TCP SYN, Telnet filters)

</td>
<td width="40%" align="center">

![NS](https://img.shields.io/badge/-Wireshark-8957e5?style=flat-square)
![NS](https://img.shields.io/badge/-Packet%20Analysis-8957e5?style=flat-square)
![NS](https://img.shields.io/badge/-Network%20Baseline-8957e5?style=flat-square)
![NS](https://img.shields.io/badge/-Protocol%20Analysis-8957e5?style=flat-square)

**Status:** `Complete`

</td>
</tr>
</table>

---

## Repository Structure

```
.
├── README.md                              ← You are here
│
├── GRC_report/
│   └── botium_toys_audit_&_risk_assessment/   ← Full GRC audit project
│       ├── audit/                             Audit findings & report
│       ├── compliance/                        Compliance matrix & gap analysis
│       ├── controls/                          Controls assessment checklist
│       ├── risk-management/                   Risk assessment & risk register
│       ├── policies/                          Access control & password policies
│       ├── implementation/                    MFA implementation plan
│       ├── reports/                           Executive summary & NIST maturity
│       └── templates/                         Reusable audit & compliance templates
│
├── Incident_analysis/
│   ├── linux_forensics_sql_threat_hunting/    ← Linux forensics & SQL threat hunting
│   │   ├── README.md
│   │   └── linux-forensics-sql-threat-hunting.md
│   ├── incident_timeline/                 ← Incident timeline reconstruction
│   └── phishing_analysis/                 ← Phishing email forensics
│       ├── README.md
│       ├── Phishing_Analysis_Report.md
│       ├── images/                        URL reputation screenshots
│       │   ├── virustotal.png
│       │   ├── ciscotalos.png
│       │   ├── brightcloud.png
│       │   └── site.png
│       └── sample/
│           └── sample-10.eml
│
├── Network_security/
│   └── Network_Baseline/                  ← Wireshark traffic baseline analysis
│
└── Playbook/
    └── phishing_ir_playbook/              ← Email phishing IR playbook
```

---

## Frameworks & Standards Applied

| Framework | Applied In |
|---|---|
| [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) — Incident Handling | Phishing Playbook · Linux Forensics |
| [NIST Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework) | Botium Toys Audit |
| [MITRE ATT&CK — T1110, T1078, T1136, T1190, T1048](https://attack.mitre.org/) | Linux Forensics · Phishing Playbook |
| [MITRE ATT&CK — T1566.001, T1566.002, T1598.003, T1204.001](https://attack.mitre.org/) | Phishing Email Analysis |
| [OWASP — SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) | Linux Forensics & SQL Threat Hunting |
| [PCI-DSS v4.0](https://www.pcisecuritystandards.org) | Botium Toys Audit · Phishing Playbook |
| [GDPR Article 33](https://gdpr-info.eu/art-33-gdpr/) | Botium Toys Audit · Phishing Playbook · Linux Forensics |
| [SOC 2 Trust Services Criteria](https://www.aicpa.org) | Botium Toys Audit |
| [CIS Controls v8](https://www.cisecurity.org/controls/) | Botium Toys Controls Assessment |

---



## How to Navigate This Repo

Every project directory contains its own `README.md` that explains:
- What the project is and why it was built
- The scenario or context (company, threat, environment)
- The framework or methodology applied
- A guide to reading the files in that directory

Start with any project's `README.md` before opening the technical documents.

---

## Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dipesh-sapkota-740b5612b/?skipRedirect=true)

---

<div align="center">

*All company names, scenarios, and organizations in this repository are fictional and created for educational purposes.*

</div>