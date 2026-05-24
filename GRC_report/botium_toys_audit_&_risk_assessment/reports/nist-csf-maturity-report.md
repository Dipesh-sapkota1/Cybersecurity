# NIST CSF Maturity Assessment Report — Botium Toys

**Document Type:** NIST Cybersecurity Framework Maturity Scorecard
**Classification:** Confidential
**Version:** 1.0
**Framework:** NIST Cybersecurity Framework (CSF) v1.1
**Scoring Scale:** 1 = Non-existent → 5 = Optimized

---

## Maturity Scale Reference

| Score | Tier | Description |
|-------|------|-------------|
| 1 | Non-existent | No formal process; function is absent |
| 2 | Ad hoc / Partial | Informal activity occurs; not consistently applied |
| 3 | Risk-Informed | Practices defined; applied inconsistently |
| 4 | Repeatable | Processes documented, approved, and consistently applied |
| 5 | Optimized | Processes continuously improved; metrics-driven |

---

## Overall Maturity Scorecard

| CSF Function | Score | Tier | Visual |
|-------------|-------|------|--------|
| **IDENTIFY** | 2 / 5 | Ad hoc | ██░░░░░░░░ |
| **PROTECT** | 2.5 / 5 | Partial | ███░░░░░░░ |
| **DETECT** | 1 / 5 | Non-existent | █░░░░░░░░░ |
| **RESPOND** | 1 / 5 | Non-existent | █░░░░░░░░░ |
| **RECOVER** | 1 / 5 | Non-existent | █░░░░░░░░░ |
| **OVERALL** | **1.5 / 5** | **Significant Gaps** | |

---

## IDENTIFY — Score: 2 / 5

**What exists:** A list of current assets has been compiled by the IT Department.

**What is missing:**
- No formal asset classification or sensitivity labeling
- No business impact analysis (BIA) performed for asset loss scenarios
- No inventory of data flows or third-party connections
- No formal risk management policy

**Evidence Supporting Score:**
- Asset list covers hardware, software, and services but lacks classification
- No determination of which asset loss would affect business continuity
- Risk assessment was reactive rather than proactive

**Target State:** Asset inventory fully classified by criticality and sensitivity (NIST CSF ID.AM)

---

## PROTECT — Score: 2.5 / 5

**What exists:**
- Firewall with defined rule set (PR.AC)
- Antivirus software installed and monitored (PR.DS)
- Physical security controls: locks, CCTV, fire suppression (PR.IP)

**What is missing:**
- No encryption at rest or in transit (PR.DS-1, PR.DS-2)
- No Least Privilege or Separation of Duties (PR.AC-4)
- No MFA for any system access (PR.AC-7)
- Password policy exists but is non-compliant and unenforced (PR.AC-1)
- No centralized identity management system (PR.AC-6)

**Evidence Supporting Score:**
- Firewall rules maintained — partial protection credit
- AV installed — partial detection/protection credit
- Complete failure on data protection and access management

**Target State:** Full implementation of access controls, encryption, and identity management

---

## DETECT — Score: 1 / 5

**What exists:**
- Antivirus with monitoring capability provides minimal detection value

**What is missing:**
- No Intrusion Detection System (IDS) — (DE.CM-1)
- No Security Information and Event Management (SIEM) platform
- No centralized log management or anomaly alerting
- No file integrity monitoring

**Evidence Supporting Score:**
- A threat actor bypassing the firewall would go entirely undetected
- No capability to identify malicious lateral movement or data exfiltration in progress

**Target State:** IDS/IPS deployed, SIEM implemented, log analysis automated with alerting

---

## RESPOND — Score: 1 / 5

**What exists:**
- EU customer breach notification plan (72-hour GDPR requirement) documented

**What is missing:**
- No formal Incident Response Plan (IRP) (RS.RP-1)
- No technical remediation playbooks for active breaches
- No defined roles or responsibilities during an incident
- No tabletop exercises or IRP testing

**Evidence Supporting Score:**
- Only regulatory notification obligations documented; no technical response capability exists

**Target State:** Documented and tested IRP with defined escalation paths, playbooks, and RACI chart

---

## RECOVER — Score: 1 / 5

**What exists:**
- IT Department maintains basic data integrity controls for day-to-day operations

**What is missing:**
- No Disaster Recovery Plan (DRP) (RC.RP-1)
- No Business Continuity Plan (BCP)
- No critical data backups of any kind
- No Recovery Time Objective (RTO) or Recovery Point Objective (RPO) defined
- No tested restoration procedures

**Evidence Supporting Score:**
- A destructive attack (ransomware, hardware failure) would result in complete and irrecoverable data loss

**Target State:** Defined DRP with tested backups, documented RTO/RPO, and cloud or offsite recovery capability

---

## Maturity Gap Summary Table

| Function | Current | Target | Gap |
|----------|---------|--------|-----|
| IDENTIFY | 2 | 4 | -2 |
| PROTECT | 2.5 | 4 | -1.5 |
| DETECT | 1 | 4 | -3 |
| RESPOND | 1 | 4 | -3 |
| RECOVER | 1 | 4 | -3 |

---

## Recommended Improvement Roadmap

### Immediate (0–30 days)
- Deploy IDS on internal network
- Implement encryption for cardholder data at rest and in transit
- Begin MFA rollout for critical systems (see `implementation/mfa-implementation-plan.md`)
- Enforce access restrictions on PII and cardholder data

### Short-Term (30–90 days)
- Implement centralized password management
- Document Incident Response Plan with tested playbooks
- Perform critical data backups; establish backup schedule

### Medium-Term (90–180 days)
- Deploy SIEM for centralized log management and alerting
- Complete asset classification and formal risk register
- Develop Disaster Recovery Plan and test restoration procedures
- Define Separation of Duties and role-based access model

### Long-Term (180+ days)
- Achieve PCI DSS compliance readiness
- Conduct third-party penetration test
- Establish formal security awareness training program
- Implement continuous monitoring and metrics reporting
