# Internal Security Audit Report — Botium Toys

**Document Type:** Internal Audit Report
**Classification:** Confidential
**Audit Type:** Security Audit & Compliance Simulation
**Engagement:** Botium Fintech Inc. / Botium Toys Pre-PCI DSS Audit Assessment
**Version:** 1.0
**Prepared By:** Security Consulting Team

---

## 1. Engagement Overview

Botium Toys engaged a security consulting team to conduct an internal security audit prior to a formal PCI DSS compliance audit. The consultant team applied the **NIST Cybersecurity Framework (CSF)** to assess organizational maturity, the **CIA Triad** to identify data security gaps, and produced a prioritized remediation report.

---

## 2. NIST CSF Maturity Scores

| Function | Score | Evidence Summary |
|----------|-------|-----------------|
| IDENTIFY | 2 / 5 | Asset list compiled without formal classification; no BIA performed |
| PROTECT | 2.5 / 5 | Firewall and AV active; encryption, IAM, and MFA absent |
| DETECT | 1 / 5 | No IDS; no SIEM; AV provides minimal detection capability only |
| RESPOND | 1 / 5 | 72-hr GDPR notification plan only; no IRP or response playbooks |
| RECOVER | 1 / 5 | No DRP, no backups; full data loss possible after any destructive event |

**Overall Maturity: 1.5 / 5 — Significant Improvement Required**

---

## 3. CIA Triad Analysis

### 3.1 Confidentiality

| Risk | Description |
|------|-------------|
| **No Least Privilege / IAM** | All employees have unrestricted access to PII, SPII, and cardholder data. A single compromised account exposes the entire dataset. |
| **No Encryption** | Customer credit card numbers stored and transmitted in plaintext. Any network capture or database access yields full cardholder data. |
| **Weak Password Policy** | Nominal password requirements with no centralized enforcement. Credential stuffing and brute-force attacks have a high probability of success. |

### 3.2 Integrity

| Risk | Description |
|------|-------------|
| **No Encryption** | Plaintext data in transit is vulnerable to man-in-the-middle attacks enabling undetected data modification. |
| **No IDS** | Malicious actors who bypass the firewall can modify data records without triggering any alert. |
| **No Access Controls** | Unrestricted internal access allows any employee — malicious or negligent — to alter records without detection. |

### 3.3 Availability

| Risk | Description |
|------|-------------|
| **No Access Controls** | Insider threat or ransomware using an employee account can lock, delete, or encrypt all business data. |
| **No DRP / BCP** | A hardware failure, ransomware attack, or natural disaster would result in permanent business disruption with no recovery path. |
| **No Data Backups** | Complete data loss is possible with no restoration capability. All customer records, transaction history, and business data would be unrecoverable. |

---

## 4. Prioritized Remediation Report

### Finding #1 — No Data Encryption

| Field | Detail |
|-------|--------|
| **Gap** | No encryption at rest or in transit for cardholder data and PII |
| **Business Risk** | Threat actors can steal credit card data and PII via database access or network interception. Results in regulatory fines up to €20M (GDPR) or 4% global turnover, payment processor termination (PCI DSS), reputational damage, and class action liability. |
| **Recommended Control** | Implement AES-256 encryption for data at rest; TLS 1.2+ for data in transit. Deploy hardware security modules (HSM) for key management. Adopt zero-trust network model. Enforce encrypted VPN for all sensitive data transport. |
| **Framework Reference** | NIST SP 800-53 SC-28 (Protection of Information at Rest), SC-8 (Transmission Confidentiality) |
| **Priority** | 🔴 Critical |

---

### Finding #2 — No Intrusion Detection System (IDS)

| Field | Detail |
|-------|--------|
| **Gap** | No IDS/IPS deployed on the internal network |
| **Business Risk** | Advanced Persistent Threats (APTs) can maintain extended dwell time without detection. Ransomware deployed internally goes unnoticed until full encryption occurs. No forensic trail available for incident investigation. Regulatory bodies will impose greater fines for failure to detect known attacks. |
| **Recommended Control** | Deploy network-based IDS (e.g., Snort, Suricata, or commercial equivalent such as Darktrace/CrowdStrike). Configure alerts for lateral movement, data exfiltration, and known attack signatures. Integrate with SIEM for centralized alerting. Provide IDS monitoring training to IT staff. |
| **Framework Reference** | NIST SP 800-53 SI-4 (System Monitoring) |
| **Priority** | 🔴 Critical |

---

### Finding #3 — No Disaster Recovery Plan / No Backups

| Field | Detail |
|-------|--------|
| **Gap** | No DRP, no BCP, no data backups of any kind |
| **Business Risk** | Any destructive event — ransomware, hardware failure, power outage, fire — results in permanent business closure. No ability to restore customer records, transaction data, or business systems. Regulatory requirements for data availability under GDPR and PCI DSS cannot be met. |
| **Recommended Control** | Implement 3-2-1 backup strategy (3 copies, 2 media types, 1 offsite/cloud). Define RTO and RPO. Document and test DRP annually. Deploy cloud backup solution (e.g., AWS Backup, Azure Recovery Services). Implement business continuity procedures with documented escalation paths. |
| **Framework Reference** | NIST SP 800-53 CP-9 (System Backup), CP-2 (Contingency Plan) |
| **Priority** | 🔴 Critical |

---

### Finding #4 — Weak / Unenforced Password Policy

| Field | Detail |
|-------|--------|
| **Gap** | Password policy exists but does not meet minimum complexity requirements; no centralized enforcement |
| **Business Risk** | Automated credential stuffing and brute-force attacks have high success probability. Weak credentials are the #1 initial access vector in ransomware campaigns. Violates PCI DSS Req. 8 and SOC 2 CC6.2, resulting in immediate audit failure. |
| **Recommended Control** | Enforce minimum 14-character passwords with complexity requirements. Deploy centralized Identity Provider (IdP) with policy enforcement (e.g., Okta, Azure AD, Duo). Screen against known breached password databases (HaveIBeenPwned API). Implement account lockout policies. Roll out security awareness training on passphrase use. |
| **Framework Reference** | NIST SP 800-53 IA-5 (Authenticator Management) |
| **Priority** | 🟠 High |

---

### Finding #5 — No Identity and Access Management (IAM) Structure

| Field | Detail |
|-------|--------|
| **Gap** | No formal IAM; no role-based access; no least privilege; no unique user ID enforcement |
| **Business Risk** | Insider threats, credential compromise, and unauthorized data access go completely unchecked. Orphaned accounts remain active post-departure. Audit investigations are hampered by no attribution trail. Fails every major compliance ITGC requirement, leading to audit failures and potential loss of operating licenses. |
| **Recommended Control** | Implement cloud IAM platform (e.g., Okta, Azure AD). Enforce unique user IDs for every account. Define role-based access model with documented Separation of Duties. Implement automated joiner-mover-leaver (JML) workflows. Conduct quarterly access reviews. |
| **Framework Reference** | NIST SP 800-53 AC-3 (Access Enforcement), IA-2 (Identification and Authentication) |
| **Priority** | 🟠 High |

---

## 5. Discussion — Legal Obligations Under Breach Scenario

### Scenario: 10,000 Customer Card Numbers Leaked

#### GDPR Obligations

- **72-Hour Rule:** Botium must notify the relevant EU Supervisory Authority within 72 hours of breach discovery (Art. 33)
- **Customer Notification:** All affected EU customers must be notified without undue delay if they face high financial risk (Art. 34)
- **Potential Fines:** Up to **€20 million or 4% of global annual turnover** (whichever is higher) for failure to implement adequate security controls (Art. 83)

#### PCI DSS Obligations

- **Mandatory Forensic Audit:** Botium must hire a certified Qualified Security Assessor (QSA) to investigate. Cost is borne by Botium.
- **Card Replacement Fees:** Botium is liable for reissuing all 10,000 compromised cards — costs absorbed by the merchant
- **Payment Processing Ban:** Failure to demonstrate remediation can result in permanent removal from card payment networks (Visa, Mastercard), destroying the e-commerce business

---

## 6. Audit Conclusion

Botium Toys presents a **high-risk security posture** with a risk score of **8/10** and an average NIST CSF maturity of **1.5/5**. The organization is **non-compliant** with PCI DSS, **partially compliant** with GDPR, and **partially compliant** with SOC 2 standards.

Immediate remediation of the five critical/high-priority findings is required before any formal third-party audit engagement. The organization should engage a dedicated security team or vCISO to oversee the remediation roadmap and track progress against the risk register.

**Overall Assessment: Significant security improvements required before audit readiness can be claimed.**
