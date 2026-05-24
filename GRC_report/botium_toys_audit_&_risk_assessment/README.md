# 🔐 Cybersecurity GRC Capstone — Botium Toys Security Audit

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Framework](https://img.shields.io/badge/Framework-NIST%20CSF-blue)
![Compliance](https://img.shields.io/badge/Compliance-PCI%20DSS%20%7C%20GDPR%20%7C%20SOC%202-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Executive Summary

This repository documents a full-scope internal security audit and GRC (Governance, Risk, and Compliance) assessment conducted for **Botium Toys**, a fictional retail and e-commerce company used as a capstone simulation. The engagement mirrors real-world enterprise security consulting work — producing a risk assessment, compliance gap analysis, controls checklist, NIST CSF maturity scoring, and a prioritized remediation roadmap.

The audit identified a **risk score of 8/10** across Botium's security program, with critical deficiencies in encryption, identity and access management, intrusion detection, and business continuity planning. This project demonstrates applied GRC skills across the full security lifecycle: from asset inventory and risk identification through to compliance remediation and executive reporting.

---

## Objectives

- Conduct a scope-defined internal audit across Botium Toys' full IT security program
- Assess control implementation against NIST CSF, PCI DSS, GDPR, and SOC 2 requirements
- Apply the CIA Triad to identify Confidentiality, Integrity, and Availability gaps
- Score organizational maturity using the NIST Cybersecurity Framework (1–5 scale)
- Produce a prioritized 5-item remediation report with framework references
- Develop a 90-day MFA implementation plan
- Analyze legal and regulatory obligations under a simulated data breach scenario

---

## Scope

| Item | Detail |
|------|--------|
| **Organization** | Botium Toys (Botium Fintech Inc. — simulation) |
| **Audit Type** | Internal Security Audit / GRC Assessment |
| **Scope Boundary** | Entire security program — all assets, processes, and compliance obligations |
| **Assets in Scope** | On-prem equipment, employee devices, e-commerce platform, internal network, databases, legacy systems |
| **Frameworks** | NIST CSF, NIST SP 800-53, PCI DSS, GDPR, SOC 2 |
| **Engagement Type** | Capstone / Portfolio Simulation |

---

## Technologies & Frameworks Used

| Category | Details |
|----------|---------|
| **Risk Framework** | NIST Cybersecurity Framework (CSF) v1.1 |
| **Control Catalog** | NIST SP 800-53 Rev. 5 |
| **Payment Compliance** | PCI DSS v3.2.1 |
| **Privacy Regulation** | GDPR (EU) 2016/679 |
| **Trust Services** | SOC 2 Type 1 & Type 2 |
| **Risk Methodology** | Qualitative risk scoring (likelihood × impact) |
| **Documentation** | Markdown, structured audit templates |

---

## Repository Structure

```
cybersecurity-grc-capstone/
│
├── README.md                          ← This file
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CODEOWNERS
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── finding_report.md          ← Audit finding issue template
│   │   ├── control_gap.md             ← Control gap issue template
│   │   └── bug_report.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── docs/
│   └── documentation-standards.md    ← Naming, versioning, formatting standards
│
├── risk-management/
│   ├── README.md
│   ├── risk-assessment-botium-toys.md ← Full risk assessment report
│   └── risk-register.md               ← Risk register with scoring
│
├── compliance/
│   ├── README.md
│   ├── compliance-matrix.md           ← Master compliance status matrix
│   ├── control-mapping.md             ← NIST → PCI DSS → GDPR cross-mapping
│   └── gap-analysis.md                ← Current state vs. required state
│
├── audit/
│   ├── README.md
│   ├── audit-report-botium-toys.md    ← Full audit findings report
│   └── audit-findings-summary.md      ← Executive-level findings summary
│
├── controls/
│   ├── README.md
│   └── controls-assessment-checklist.md ← Controls & compliance checklist
│
├── policies/
│   ├── README.md
│   ├── password-policy.md
│   └── access-control-policy.md
│
├── evidence/
│   ├── README.md
│   └── evidence-collection-standards.md
│
├── implementation/
│   ├── README.md
│   └── mfa-implementation-plan.md     ← 90-day MFA rollout plan
│
├── reports/
│   ├── README.md
│   ├── executive-summary.md           ← C-suite facing summary
│   └── nist-csf-maturity-report.md    ← NIST CSF maturity scorecard
│
├── templates/
│   ├── risk-register-template.md
│   ├── audit-checklist-template.md
│   ├── compliance-checklist-template.md
│   ├── security-control-assessment-template.md
│   ├── vulnerability-tracking-template.md
│   ├── incident-report-template.md
│   ├── change-management-template.md
│   └── evidence-collection-template.md
│
├── references/
│   ├── README.md
│   └── framework-references.md
│
├── diagrams/
│   └── README.md                      ← Placeholder for architecture diagrams
│
└── appendices/
    └── README.md
```

---

## Key Deliverables

| Deliverable | Location | Status |
|------------|----------|--------|
| Risk Assessment Report | `risk-management/risk-assessment-botium-toys.md` | ✅ Complete |
| Risk Register | `risk-management/risk-register.md` | ✅ Complete |
| Controls Assessment Checklist | `controls/controls-assessment-checklist.md` | ✅ Complete |
| Compliance Matrix (PCI DSS, GDPR, SOC 2) | `compliance/compliance-matrix.md` | ✅ Complete |
| Control Mapping (NIST → PCI DSS → GDPR) | `compliance/control-mapping.md` | ✅ Complete |
| Gap Analysis | `compliance/gap-analysis.md` | ✅ Complete |
| NIST CSF Maturity Scorecard | `reports/nist-csf-maturity-report.md` | ✅ Complete |
| Audit Report | `audit/audit-report-botium-toys.md` | ✅ Complete |
| Prioritized Remediation Report | `audit/audit-findings-summary.md` | ✅ Complete |
| Executive Summary | `reports/executive-summary.md` | ✅ Complete |
| 90-Day MFA Implementation Plan | `implementation/mfa-implementation-plan.md` | ✅ Complete |
| Reusable Templates (8) | `templates/` | ✅ Complete |

---

## Methodology

This engagement follows the **NIST Cybersecurity Framework (CSF)** five core functions as the primary audit methodology:

```
IDENTIFY → PROTECT → DETECT → RESPOND → RECOVER
```

**Phase 1 — Scoping & Asset Inventory**
Define audit boundaries, identify all assets in scope, classify by sensitivity and business impact.

**Phase 2 — Risk Assessment**
Apply qualitative risk scoring. Evaluate likelihood and potential business impact for each identified gap.

**Phase 3 — Controls Assessment**
Evaluate implementation status of administrative, technical, and physical security controls against NIST SP 800-53 and industry benchmarks.

**Phase 4 — Compliance Review**
Map controls to PCI DSS, GDPR, and SOC 2 requirements. Identify non-compliant areas and document evidence.

**Phase 5 — Gap Analysis & Remediation Planning**
Produce prioritized findings. Assign risk ratings (Critical / High / Medium / Low). Map each gap to a framework control reference.

**Phase 6 — Reporting**
Deliver executive summary, detailed audit report, and actionable remediation roadmap.

---

## NIST CSF Maturity Scores — Botium Toys

| CSF Function | Score (1–5) | Interpretation |
|-------------|------------|----------------|
| **Identify** | 2 / 5 | Asset list exists; no formal classification |
| **Protect** | 2.5 / 5 | Partial controls (firewall, AV); no encryption or IAM |
| **Detect** | 1 / 5 | No IDS, no SIEM |
| **Respond** | 1 / 5 | 72-hr breach notification only; no IRP |
| **Recover** | 1 / 5 | No DRP, no backups |
| **Overall** | **1.5 / 5** | **Significant improvement required** |

---

## Top 5 Prioritized Remediation Items

| Priority | Gap | Risk Level | Framework Reference |
|---------|-----|-----------|-------------------|
| 1 | No data encryption (at rest & in transit) | 🔴 Critical | NIST SP 800-53 SC-28, SC-8 |
| 2 | No Intrusion Detection System (IDS) | 🔴 Critical | NIST SP 800-53 SI-4 |
| 3 | No Disaster Recovery Plan / Backups | 🔴 Critical | NIST SP 800-53 CP-9, CP-2 |
| 4 | No Password Policy Enforcement | 🟠 High | NIST SP 800-53 IA-5 |
| 5 | No IAM / Least Privilege Structure | 🟠 High | NIST SP 800-53 AC-3, IA-2 |

---

## Security Controls Overview

### Administrative Controls
- [ ] Least Privilege Policy
- [ ] Separation of Duties
- [ ] Disaster Recovery Plan
- [ ] Incident Response Plan
- [x] 72-Hour Breach Notification Procedure (GDPR)
- [x] Privacy Policies Documented

### Technical Controls
- [x] Firewall (rule-based traffic filtering)
- [x] Antivirus Software (installed & monitored)
- [ ] Intrusion Detection System (IDS)
- [ ] Data Encryption (at rest & in transit)
- [ ] Password Management System (compliant)
- [ ] Multi-Factor Authentication (MFA)
- [ ] Centralized Logging / SIEM

### Physical Controls
- [x] Locks (offices, warehouse, storefront)
- [x] CCTV Surveillance (monitored)
- [x] Fire Detection & Suppression Systems

---

## Architecture Overview

```
┌─────────────────────────────────────────────┐
│              BOTIUM TOYS ENVIRONMENT         │
│                                             │
│  ┌──────────┐    ┌──────────┐    ┌────────┐ │
│  │ Internet │───▶│ Firewall │───▶│ LAN    │ │
│  └──────────┘    └──────────┘    └────────┘ │
│                                      │       │
│              ┌───────────────────────┤       │
│              │                       │       │
│         ┌────▼─────┐          ┌──────▼────┐  │
│         │ Ecommerce│          │ Internal  │  │
│         │ Platform │          │ Database  │  │
│         └──────────┘          └───────────┘  │
│                                             │
│  ⚠️  GAPS: No IDS, No Encryption, No MFA    │
└─────────────────────────────────────────────┘
```

> Full architecture diagrams are maintained in the `/diagrams` directory.

---

## Skills Demonstrated

| Domain | Skills |
|--------|--------|
| **GRC** | Risk assessment, compliance mapping, gap analysis, audit reporting |
| **Frameworks** | NIST CSF, NIST SP 800-53, PCI DSS, GDPR, SOC 2 |
| **Risk Management** | Qualitative risk scoring, risk register management, business impact analysis |
| **Security Controls** | Administrative, technical, and physical control assessment |
| **Compliance** | PCI DSS requirements, GDPR obligations, SOC 2 trust principles |
| **Audit** | Audit scoping, evidence collection, findings documentation, executive reporting |
| **IAM** | Least privilege, separation of duties, MFA implementation planning |
| **Incident Response** | Breach notification obligations, 72-hour GDPR requirement |
| **Technical Writing** | Markdown documentation, executive summaries, policy writing |

---

## Future Improvements

- [ ] Add architecture diagrams (network topology, data flow)
- [ ] Develop full Incident Response Plan (IRP)
- [ ] Build SIEM implementation playbook
- [ ] Create vendor/third-party risk assessment template
- [ ] Expand to ISO 27001 control mapping
- [ ] Add vulnerability management program documentation
- [ ] Develop Security Awareness Training program outline
- [ ] Produce Business Continuity Plan (BCP)

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## Author

**Dipesh Sapkota**
Cybersecurity Analyst | GRC Consultant | Security Researcher

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/dipesh-sapkota-740b5612b/?skipRedirect=true)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Dipesh-sapkota1)

> *This project was completed as part of a cybersecurity governance and compliance capstone. All company names and data are fictional and used for educational purposes only.*
