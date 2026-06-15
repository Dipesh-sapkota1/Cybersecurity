# 📧 Phishing Email Analysis – Capstone Project

A  cybersecurity project analyzing a real-world phishing email sample. This repository documents the investigation process, findings, and indicators of compromise (IOCs) from a static email forensics exercise.

---

## 📁 Repository Structure

```
├── README.md                    # This file
├── Phishing_Analysis_Report.md  # Full analysis report
└── sample/
    └── sample-10.eml            # Source email sample (from phishing_pot)
```

---

## 🔍 Sample Overview

| Field          | Value                                                              |
| -------------- | ------------------------------------------------------------------ |
| File           | `sample-10.eml`                                                    |
| Source         | [rf-peixoto/phishing\_pot](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-10.eml) |
| SHA256         | `4fbf4c3d80aba156c59004c12c83ff53dd64c9cf7b7a6029e98fe1da0760783a` |
| Analysis Type  | Static Phishing Email Investigation                                |

---

## 🎯 What This Project Covers

- Email header inspection (From, Reply-To, Return-Path, Sender IP)
- Sender domain and hosting infrastructure analysis
- Social engineering technique identification
- URL defanging and reputation checking
- IOC extraction and documentation
- MITRE ATT&CK technique mapping

---

## ⚠️ Key Findings

- Sender impersonates the **Microsoft account security team** using a fake domain (`access-accsecurity.com`)
- `Reply-To` redirects to an attacker-controlled Gmail account (`sotrecognizd@gmail.com`)
- Embedded tracking URL flagged as malicious on VirusTotal (domain: `thebandalisty.com`)
- A deceptive `mailto:` anchor tag is disguised as a "Report The User" security feature
- No email authentication (SPF/DKIM/DMARC) observed
- No malicious attachment or credential harvesting page found — likely a tracking/reconnaissance campaign

---

## 🗂️ MITRE ATT&CK Techniques

| ID         | Technique                          |
| ---------- | ---------------------------------- |
| T1566.001  | Phishing: Spearphishing via Service |
| T1566.002  | Phishing: Spearphishing Link       |
| T1598.003  | Phishing for Information           |
| T1204.001  | User Execution: Malicious Link     |

---

## 📄 Full Report

The complete analysis is in [`Phishing_Analysis_Report.md`](./Phishing_Analysis_Report.md), which includes:

- Header analysis table
- Sender infrastructure breakdown
- Content and social engineering observations
- URL analysis with reputation screenshot placeholder
- Full IOC table
- MITRE ATT&CK mapping with explanations
- Conclusions and references

---

## 🛠️ Tools Referenced

- [VirusTotal](https://www.virustotal.com) – URL and domain reputation
- [URLVoid](https://www.urlvoid.com) – Domain reputation
- [Cisco Talos](https://talosintelligence.com) – Threat intelligence
- [MITRE ATT&CK](https://attack.mitre.org) – Technique mapping

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The email sample was sourced from a public phishing honeypot repository. No malicious infrastructure was interacted with beyond passive reputation lookups.

---

## 👤 Author

Cybersecurity Student – Capstone Project
