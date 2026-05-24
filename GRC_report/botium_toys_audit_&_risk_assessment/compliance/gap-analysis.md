# Gap Analysis — Botium Toys

**Document Type:** Security Gap Analysis
**Classification:** Confidential
**Version:** 1.0
**Methodology:** Current State vs. Required State (NIST CSF / PCI DSS / GDPR)

---

## Purpose

This gap analysis identifies the delta between Botium Toys' current security posture and the controls required by applicable frameworks. Each gap includes a description of the current state, the required state, the business justification, and an effort/impact rating to aid prioritization.

---

## Gap Analysis Table

### Data Protection

| Gap ID | Control Area | Current State | Required State | Business Justification | Effort | Impact |
|--------|------------|--------------|---------------|----------------------|--------|--------|
| GAP-001 | Encryption at Rest | No encryption; cardholder data stored in plaintext local database | AES-256 encryption for all PII and cardholder data at rest | Eliminates data theft risk from database compromise | Medium | Critical |
| GAP-002 | Encryption in Transit | No TLS/SSL enforced for data transmission | TLS 1.2+ for all data in transit | Eliminates man-in-the-middle attack risk | Medium | Critical |

---

### Access Control & Identity Management

| Gap ID | Control Area | Current State | Required State | Business Justification | Effort | Impact |
|--------|------------|--------------|---------------|----------------------|--------|--------|
| GAP-003 | Least Privilege | All employees have unrestricted access to all data including PII/SPII | Role-based access; employees access only data required for their role | Limits blast radius of any compromised account | Medium | Critical |
| GAP-004 | Separation of Duties | No documented role separation | High-risk actions require two independent approvals | Prevents insider fraud and unilateral high-risk actions | High | High |
| GAP-005 | MFA | No MFA on any system | MFA required for all access to cardholder data environments and remote systems | Single most effective control against credential-based attacks | Medium | High |
| GAP-006 | Password Policy Enforcement | Policy exists; below minimum complexity; no central enforcement | Minimum 14-character policy with complexity rules, enforced via IAM platform | Eliminates automated credential attack success | Low | High |
| GAP-007 | Centralized IAM | No identity management platform | Cloud or hybrid IAM with JML workflows, unique user IDs, access reviews | Enables auditability, access governance, and offboarding automation | High | High |

---

### Detection & Monitoring

| Gap ID | Control Area | Current State | Required State | Business Justification | Effort | Impact |
|--------|------------|--------------|---------------|----------------------|--------|--------|
| GAP-008 | Intrusion Detection | No IDS deployed | Network-based IDS/IPS with alerting | Detects active attacks that bypass the firewall | Medium | Critical |
| GAP-009 | SIEM / Log Management | No centralized logging | SIEM platform aggregating logs with correlation rules and alerting | Enables incident detection, investigation, and compliance audit trail | High | High |

---

### Incident Response & Recovery

| Gap ID | Control Area | Current State | Required State | Business Justification | Effort | Impact |
|--------|------------|--------------|---------------|----------------------|--------|--------|
| GAP-010 | Incident Response Plan | 72-hour GDPR notification only | Full IRP with playbooks, RACI, escalation procedures, and tabletop testing | Ensures structured, compliant, and rapid response to incidents | Medium | High |
| GAP-011 | Disaster Recovery Plan | No DRP | Documented, tested DRP with defined RTO and RPO | Ensures business survival after any destructive event | Medium | Critical |
| GAP-012 | Data Backups | No backups | 3-2-1 backup strategy; tested restoration procedures | Eliminates irrecoverable data loss scenario | Low | Critical |

---

### Asset Management

| Gap ID | Control Area | Current State | Required State | Business Justification | Effort | Impact |
|--------|------------|--------------|---------------|----------------------|--------|--------|
| GAP-013 | Asset Classification | Asset list without classification | Full inventory with sensitivity, criticality, and owner labels | Foundation for all other controls; required by NIST Identify and GDPR | Low | High |
| GAP-014 | Legacy System Management | Maintained but no defined schedule or playbook | Defined maintenance schedule; documented intervention procedures | Reduces risk of undetected compromise of unpatched legacy systems | Low | Medium |

---

## Prioritization Matrix

| Priority | Gap IDs | Rationale |
|---------|---------|-----------|
| 🔴 Immediate (0–30 days) | GAP-001, GAP-002, GAP-003, GAP-005, GAP-008 | Direct exposure of cardholder data and PII |
| 🟠 Short-Term (30–90 days) | GAP-006, GAP-010, GAP-011, GAP-012 | Business continuity and compliance |
| 🟡 Medium-Term (90–180 days) | GAP-004, GAP-007, GAP-009, GAP-013 | Governance and long-term compliance readiness |
| 🟢 Long-Term (180+ days) | GAP-014 | Operational hygiene improvement |

---

## Effort vs. Impact Summary

| Gap | Effort | Impact | Priority Score |
|-----|--------|--------|---------------|
| GAP-012 — Data Backups | Low | Critical | ⭐⭐⭐⭐⭐ |
| GAP-013 — Asset Classification | Low | High | ⭐⭐⭐⭐ |
| GAP-006 — Password Policy | Low | High | ⭐⭐⭐⭐ |
| GAP-001 — Encryption at Rest | Medium | Critical | ⭐⭐⭐⭐⭐ |
| GAP-002 — Encryption in Transit | Medium | Critical | ⭐⭐⭐⭐⭐ |
| GAP-003 — Least Privilege | Medium | Critical | ⭐⭐⭐⭐⭐ |
| GAP-005 — MFA | Medium | High | ⭐⭐⭐⭐ |
| GAP-008 — IDS | Medium | Critical | ⭐⭐⭐⭐⭐ |
| GAP-010 — IRP | Medium | High | ⭐⭐⭐⭐ |
| GAP-011 — DRP | Medium | Critical | ⭐⭐⭐⭐⭐ |
| GAP-004 — Separation of Duties | High | High | ⭐⭐⭐ |
| GAP-007 — Centralized IAM | High | High | ⭐⭐⭐ |
| GAP-009 — SIEM | High | High | ⭐⭐⭐ |
| GAP-014 — Legacy System Mgmt | Low | Medium | ⭐⭐⭐ |
