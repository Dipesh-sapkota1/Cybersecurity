# Risk Register — Botium Toys

**Document Type:** Risk Register
**Classification:** Confidential — Internal Use Only
**Version:** 1.0
**Last Updated:** [Insert Date]

---

## Risk Scoring Methodology

| Score | Likelihood | Impact |
|-------|-----------|--------|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost Certain | Catastrophic |

**Risk Level = Likelihood × Impact**

| Score | Rating |
|-------|--------|
| 1–4 | 🟢 Low |
| 5–9 | 🟡 Medium |
| 10–16 | 🟠 High |
| 17–25 | 🔴 Critical |

---

## Risk Register

| ID | Risk Title | Category | Description | Likelihood | Impact | Score | Rating | Owner | Status | Control Reference |
|----|-----------|----------|-------------|-----------|--------|-------|--------|-------|--------|------------------|
| R-001 | Unencrypted PII/Cardholder Data | Data Protection | Customer credit card data stored and transmitted in plaintext in internal database | 5 | 5 | 25 | 🔴 Critical | IT Manager | Open | NIST SC-28, SC-8 / PCI DSS Req 3, 4 |
| R-002 | No Intrusion Detection | Network Security | No IDS/IPS deployed; malicious traffic bypassing firewall goes undetected | 4 | 5 | 20 | 🔴 Critical | IT Manager | Open | NIST SI-4 |
| R-003 | No Disaster Recovery Plan | Business Continuity | No DRP, BCP, or critical data backups; full data loss possible after incident | 3 | 5 | 15 | 🟠 High | IT Manager | Open | NIST CP-2, CP-9 |
| R-004 | Unrestricted Employee Data Access | Access Control | All employees can access PII/SPII and cardholder data; no least privilege enforced | 5 | 4 | 20 | 🔴 Critical | IT Manager | Open | NIST AC-3, AC-6 |
| R-005 | No Separation of Duties | IAM | No hierarchical role structure; single employees can perform high-risk actions unchecked | 4 | 4 | 16 | 🟠 High | HR / IT | Open | NIST AC-5 |
| R-006 | Weak Password Policy | Credential Management | Password policy exists but below minimum complexity; no centralized enforcement | 4 | 3 | 12 | 🟠 High | IT Manager | Open | NIST IA-5 / PCI DSS Req 8 |
| R-007 | No MFA | Authentication | Multi-factor authentication absent from all critical systems | 4 | 4 | 16 | 🟠 High | IT Manager | Open | NIST IA-2 |
| R-008 | Legacy System Risk | System Lifecycle | End-of-life systems monitored but no defined schedule or intervention playbook | 3 | 3 | 9 | 🟡 Medium | IT Manager | Open | NIST SA-22 |
| R-009 | GDPR Non-Compliance | Regulatory | EU customer data not properly secured; asset classification missing | 4 | 5 | 20 | 🔴 Critical | Legal / IT | Open | GDPR Art. 32, 33 |
| R-010 | PCI DSS Non-Compliance | Regulatory | Multiple PCI DSS requirements unmet; risk of audit failure and payment processing ban | 5 | 5 | 25 | 🔴 Critical | Legal / IT | Open | PCI DSS Req 3, 4, 7, 8 |
| R-011 | No SIEM / Centralized Logging | Detection | No centralized log management; no visibility into anomalies or attack patterns | 4 | 4 | 16 | 🟠 High | IT Manager | Open | NIST SI-4, AU-2 |
| R-012 | No Incident Response Plan | Incident Management | Technical IRP absent; no playbooks for breach response or legacy system incidents | 3 | 4 | 12 | 🟠 High | IT Manager | Open | NIST IR-4, IR-8 |

---

## Risk Summary by Category

| Category | Critical | High | Medium | Low | Total |
|----------|---------|------|--------|-----|-------|
| Data Protection | 1 | 0 | 0 | 0 | 1 |
| Network Security | 1 | 0 | 0 | 0 | 1 |
| Business Continuity | 0 | 1 | 0 | 0 | 1 |
| Access Control | 1 | 1 | 0 | 0 | 2 |
| IAM | 0 | 2 | 0 | 0 | 2 |
| Credential Management | 0 | 1 | 0 | 0 | 1 |
| Detection | 1 | 1 | 0 | 0 | 2 |
| Regulatory | 2 | 0 | 0 | 0 | 2 |
| System Lifecycle | 0 | 0 | 1 | 0 | 1 |
| Incident Management | 0 | 1 | 0 | 0 | 1 |
| **Total** | **6** | **7** | **1** | **0** | **14** |

---

## Residual Risk Targets (Post-Remediation)

| ID | Current Rating | Target Rating | Target Date |
|----|---------------|--------------|------------|
| R-001 | 🔴 Critical | 🟢 Low | Q1 |
| R-002 | 🔴 Critical | 🟢 Low | Q1 |
| R-003 | 🟠 High | 🟢 Low | Q2 |
| R-004 | 🔴 Critical | 🟢 Low | Q1 |
| R-005 | 🟠 High | 🟡 Medium | Q2 |
| R-006 | 🟠 High | 🟢 Low | Q1 |
| R-007 | 🟠 High | 🟢 Low | Q1 |
| R-008 | 🟡 Medium | 🟢 Low | Q3 |
| R-009 | 🔴 Critical | 🟢 Low | Q1 |
| R-010 | 🔴 Critical | 🟢 Low | Q1 |
| R-011 | 🟠 High | 🟡 Medium | Q2 |
| R-012 | 🟠 High | 🟡 Medium | Q2 |
