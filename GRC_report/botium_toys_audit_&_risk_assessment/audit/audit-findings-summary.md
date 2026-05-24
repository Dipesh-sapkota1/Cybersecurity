# Audit Findings Summary — Botium Toys

**Document Type:** Executive Findings Summary
**Classification:** Confidential
**Version:** 1.0

---

## Findings Overview

| Finding ID | Title | Severity | Framework Ref | Status |
|-----------|-------|---------|--------------|--------|
| FIND-001 | No Data Encryption (at rest and in transit) | 🔴 Critical | NIST SC-28, SC-8 / PCI DSS Req. 3, 4 | Open |
| FIND-002 | No Intrusion Detection System (IDS) | 🔴 Critical | NIST SI-4 / PCI DSS Req. 11 | Open |
| FIND-003 | No Disaster Recovery Plan / No Backups | 🔴 Critical | NIST CP-9, CP-2 | Open |
| FIND-004 | Unrestricted Employee Access to PII and Cardholder Data | 🔴 Critical | NIST AC-3, AC-6 / PCI DSS Req. 7 | Open |
| FIND-005 | Weak and Unenforced Password Policy | 🟠 High | NIST IA-5 / PCI DSS Req. 8 | Open |
| FIND-006 | No MFA on Any System | 🟠 High | NIST IA-2 / PCI DSS Req. 8.3 | Open |
| FIND-007 | No Separation of Duties / IAM Structure | 🟠 High | NIST AC-5 / PCI DSS Req. 6 | Open |
| FIND-008 | No SIEM / Centralized Logging | 🟠 High | NIST AU-2, SI-4 / PCI DSS Req. 10 | Open |
| FIND-009 | No Incident Response Plan | 🟠 High | NIST IR-4, IR-8 | Open |
| FIND-010 | Legacy System Maintenance Gaps | 🟡 Medium | NIST SA-22 | Open |

---

## Severity Distribution

| Severity | Count |
|---------|-------|
| 🔴 Critical | 4 |
| 🟠 High | 5 |
| 🟡 Medium | 1 |
| **Total** | **10** |

---

## Positive Findings

| Control | Status | Notes |
|---------|--------|-------|
| Firewall | ✅ Implemented | Rule-based; maintained by IT |
| Antivirus Software | ✅ Implemented | Installed and monitored |
| Physical Security | ✅ Implemented | Locks, CCTV, fire suppression |
| GDPR 72-Hour Notification Plan | ✅ Implemented | Documented and enforced |
| Privacy Policies | ⚠️ Partial | Documented; not fully supported by technical controls |

---

## Compliance Posture

| Framework | Compliant | Total | % |
|-----------|---------|-------|---|
| PCI DSS | 3 | 12 | 25% |
| GDPR | 2 | 6 | 33% |
| SOC 2 | 1 | 8 | 13% |

---

## Remediation Priority

| Timeline | Findings |
|---------|---------|
| Immediate (0–30 days) | FIND-001, FIND-002, FIND-003, FIND-004 |
| Short-Term (30–90 days) | FIND-005, FIND-006, FIND-009 |
| Medium-Term (90–180 days) | FIND-007, FIND-008 |
| Long-Term (180+ days) | FIND-010 |

*Full details in `audit/audit-report-botium-toys.md`*
