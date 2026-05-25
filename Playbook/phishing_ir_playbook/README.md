# 🛡️ Email Phishing Incident Response Playbook
### NexaCore Technologies — Security Operations

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![Framework](https://img.shields.io/badge/Framework-NIST%20SP%20800--61-orange)
![Last Reviewed](https://img.shields.io/badge/Last%20Reviewed-May%202026-lightgrey)

---

## About This Project

This repository contains the official **Email Phishing Incident Response Playbook** for NexaCore Technologies, a mid-size B2B SaaS company operating in the financial technology sector.

Email phishing is consistently ranked as the **#1 initial attack vector** across all industries. For a company like NexaCore that handles sensitive client financial data, a single successful phishing attack can result in credential theft, unauthorized data access, regulatory penalties, and lasting reputational damage.

This playbook was built to give NexaCore's security team a clear, step-by-step operational guide — so that when a phishing incident occurs, responders are not making decisions from scratch under pressure.

---

## Company Profile — NexaCore Technologies

| Attribute | Details |
|---|---|
| **Industry** | Financial Technology (B2B SaaS) |
| **Employees** | ~300 |
| **Headquarters** | Austin, Texas |
| **Environment** | Microsoft 365, Azure AD, CrowdStrike EDR, Splunk SIEM |
| **Compliance Obligations** | SOC 2 Type II, PCI-DSS, GDPR (EU clients) |
| **Security Team Size** | 8 (CISO, IR Lead, 2 IR Analysts, 3 SOC Analysts, 1 IT Security Admin) |

### Why NexaCore Needs This Playbook

NexaCore processes financial transaction data for over 400 enterprise clients. This makes it a high-value target for:

- **Business Email Compromise (BEC)** — attackers impersonating executives to authorize fraudulent transfers
- **Credential harvesting** — stealing Azure AD credentials to access client financial data
- **Supply chain phishing** — impersonating NexaCore to target its clients

Without a documented response process, incidents take longer to contain, evidence gets destroyed, and compliance violations go unreported — all of which compound the damage.

---

## Repository Structure

```
phishing-ir-playbook/
│
├── README.md                          ← You are here (project overview)
│
├── playbook/
│   ├── phishing-playbook.md           ← Full incident response playbook
│   └── quick-reference-card.md        ← One-page cheat sheet for SOC analysts
│
├── diagrams/
│   └── incident-response-flow.md      ← Response workflow (Mermaid diagram)
│
├── templates/
│   ├── incident-ticket-template.md    ← Standardized incident logging template
│   └── notification-templates.md      ← Pre-written communication templates
│
└── references.md                      ← Frameworks, sources, and further reading
```

---

## Playbook Highlights

- **Framework:** NIST SP 800-61 Rev. 2 (Preparation → Detection → Containment → Recovery → Post-Incident)
- **Threat Coverage:** Credential harvesting, malware delivery, BEC, spear phishing
- **Severity Levels:** 4-tier classification (Low → Medium → High → Critical)
- **Decision-based:** Branching logic at each phase — not a flat checklist
- **Role-specific:** Every action mapped to a responsible role
- **Tool-specific:** References NexaCore's actual toolstack (Splunk, CrowdStrike, M365 Defender)
- **Compliance-aware:** GDPR and PCI-DSS notification timelines included

---

## How to Use This Playbook

| Situation | Go To |
|---|---|
| Phishing email just reported by a user | [Quick Reference Card](./quick-reference-card.md) |
| Full investigation underway | [Main Playbook](./phishing-playbook.md) |
| Need to log the incident | [Incident Ticket Template](./incident-ticket-template.md) |
| Need to notify a user or manager | [Notification Templates](./notification-templates.md) |
| Want to understand the response flow | [Incident Flow Diagram](./incident-response-flow.md) |

---

## Frameworks & Standards Referenced

- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) — Computer Security Incident Handling Guide
- [MITRE ATT&CK](https://attack.mitre.org/) — Phishing: T1566
- [CISA Phishing Guidance](https://www.cisa.gov/phishing)
- [Microsoft Security Response](https://www.microsoft.com/en-us/security) — M365 Defender documentation

---

## Document Control

| Field | Detail |
|---|---|
| **Author** | Security Operations Team, NexaCore Technologies |
| **Version** | 1.0 |
| **Created** | May 2026 |
| **Review Cycle** | Quarterly, or after any phishing incident |
| **Classification** | Internal Use Only |
| **Owner** | CISO |

---

## About This Project (For Reviewers)

This playbook was developed as a capstone project for a cybersecurity program, grounded in real-world incident response methodology. It applies NIST SP 800-61 to a realistic organizational context, demonstrating how security documentation connects to business requirements, compliance obligations, and operational tooling.

> *"A playbook is only as good as the team that maintains it. This document should be treated as a living artifact — updated after every incident and reviewed every quarter."*
