# Compliance Matrix — Botium Toys

**Document Type:** Master Compliance Status Matrix
**Version:** 1.0
**Frameworks:** PCI DSS v3.2.1 | GDPR | SOC 2 | NIST SP 800-53

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Compliant — Control implemented |
| ⚠️ | Partial — Control partially implemented |
| ❌ | Non-Compliant — Control absent |
| N/A | Not Applicable to current scope |

---

## PCI DSS Compliance Matrix

| Req # | Requirement | Status | Evidence / Finding | NIST SP 800-53 Mapping |
|-------|------------|--------|-------------------|----------------------|
| 1 | Install and maintain a firewall | ✅ | Rule-based firewall in place | SC-7 |
| 2 | Do not use vendor-supplied defaults | ⚠️ | Unknown — not assessed | CM-6 |
| 3 | Protect stored cardholder data | ❌ | No encryption; data stored in plaintext | SC-28 |
| 4 | Encrypt transmission of cardholder data | ❌ | No encryption in transit | SC-8 |
| 5 | Protect against malware | ✅ | AV software installed and monitored | SI-3 |
| 6 | Develop and maintain secure systems | ❌ | No patching schedule for legacy systems | SI-2 |
| 7 | Restrict access to cardholder data | ❌ | All employees have unrestricted access | AC-3, AC-6 |
| 8 | Identify and authenticate access | ❌ | No MFA; password policy non-compliant | IA-2, IA-5 |
| 9 | Restrict physical access | ✅ | Locks, CCTV, access controls in place | PE-3 |
| 10 | Track and monitor all access | ❌ | No SIEM or centralized logging | AU-2, SI-4 |
| 11 | Regularly test security systems | ❌ | No IDS, no pen testing performed | CA-8, SI-4 |
| 12 | Maintain an information security policy | ⚠️ | Basic policies exist; not fully enforced | PL-1 |

**PCI DSS Summary: 3 / 12 Compliant (25%)**

---

## GDPR Compliance Matrix

| Article | Requirement | Status | Evidence / Finding | NIST SP 800-53 Mapping |
|---------|------------|--------|-------------------|----------------------|
| Art. 5 | Principles of data processing | ❌ | Data not classified; no purpose limitation evidence | AC-3, MP-3 |
| Art. 25 | Data protection by design and default | ❌ | No privacy-by-design controls implemented | PL-8 |
| Art. 32 | Security of processing | ❌ | No encryption; insufficient technical measures | SC-28, SC-8 |
| Art. 33 | Notification of breach to supervisory authority | ✅ | 72-hour notification plan documented and enforced | IR-6 |
| Art. 34 | Communication of breach to data subjects | ✅ | Notification procedure established for EU customers | IR-6 |
| Art. 35 | Data protection impact assessment | ❌ | No DPIA performed | RA-3 |
| Art. 83 | Conditions for imposing fines | ⚠️ | Partial adherence; breach exposure significant | — |

**GDPR Summary: 2 / 6 Compliant (33%)**

---

## SOC 2 Trust Services Criteria Matrix

| Category | Criterion | Status | Evidence / Finding | NIST SP 800-53 Mapping |
|----------|----------|--------|-------------------|----------------------|
| **Security** | CC6.1 — Logical access controls | ❌ | No role-based access; all employees access PII | AC-3 |
| **Security** | CC6.2 — Authentication | ❌ | No MFA; weak password policy | IA-2, IA-5 |
| **Security** | CC6.3 — Access restriction | ❌ | No least privilege or separation of duties | AC-6, AC-5 |
| **Security** | CC7.1 — Monitoring | ❌ | No SIEM, no IDS | SI-4, AU-2 |
| **Availability** | A1.1 — Availability commitments | ⚠️ | IT maintains uptime; no DRP | CP-2 |
| **Availability** | A1.2 — Recovery | ❌ | No backups, no DRP tested | CP-9 |
| **Confidentiality** | C1.1 — Confidential information identified | ❌ | No asset classification | MP-3, RA-2 |
| **Confidentiality** | C1.2 — Confidential information protected | ❌ | No encryption applied | SC-28 |
| **Processing Integrity** | PI1.1 — Data integrity | ✅ | IT maintains integrity controls | SI-7 |
| **Privacy** | P3.1 — Personal information collected | ⚠️ | Privacy policies documented but data unsecured | AR-1 |

**SOC 2 Summary: 1 / 8 Criteria Fully Met (13%)**

---

## Cross-Framework Compliance Summary

| Control Area | NIST SP 800-53 | PCI DSS | GDPR | SOC 2 | Status |
|-------------|---------------|---------|------|-------|--------|
| Data Encryption | SC-28, SC-8 | Req. 3, 4 | Art. 32 | C1.2 | ❌ |
| Access Control | AC-3, AC-6 | Req. 7 | Art. 5 | CC6.1 | ❌ |
| Authentication / MFA | IA-2, IA-5 | Req. 8 | Art. 32 | CC6.2 | ❌ |
| Intrusion Detection | SI-4 | Req. 11 | Art. 32 | CC7.1 | ❌ |
| Backup / Recovery | CP-9, CP-2 | Req. 12 | Art. 32 | A1.2 | ❌ |
| Firewall | SC-7 | Req. 1 | Art. 32 | CC6 | ✅ |
| Antivirus | SI-3 | Req. 5 | Art. 32 | CC7 | ✅ |
| Physical Security | PE-3 | Req. 9 | Art. 32 | CC6 | ✅ |
| Breach Notification | IR-6 | Req. 12 | Art. 33, 34 | — | ✅ |
| Privacy Policies | AR-1 | Req. 12 | Art. 5, 25 | P3.1 | ⚠️ |
| Logging / Monitoring | AU-2, SI-4 | Req. 10 | Art. 32 | CC7.1 | ❌ |
| Incident Response | IR-4, IR-8 | Req. 12 | Art. 33 | CC7.4 | ❌ |
| Asset Classification | CM-8, RA-2 | Req. 2 | Art. 5 | C1.1 | ❌ |
