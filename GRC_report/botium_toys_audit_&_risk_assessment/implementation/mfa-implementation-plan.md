# 90-Day MFA Implementation Plan — Botium Toys

**Document Type:** Implementation Plan
**Classification:** Confidential — Internal Use Only
**Version:** 1.0
**Framework Reference:** NIST SP 800-53 IA-2, IA-5 | PCI DSS Req. 8.3 | GDPR Art. 32

---

## Executive Summary

This document outlines a phased 90-day plan to deploy Multi-Factor Authentication (MFA) across Botium Toys' systems. MFA addresses one of the organization's most critical and exploitable vulnerabilities: single-factor authentication on all systems containing sensitive customer data, PII, and cardholder information.

The plan accounts for Botium's hybrid infrastructure (on-premises and cloud/e-commerce), small IT team, limited budget, and the need to protect legacy systems that cannot natively support modern authentication apps.

---

## Recommended Solution

**Hybrid IAM Platform:** Duo Security (Cisco) or Microsoft Entra ID with On-Premises Application Proxy

**Rationale:**
- Supports on-premises servers, remote workstations, and cloud applications simultaneously
- Provides hardware security key fallback for legacy systems incompatible with smartphone apps
- Scales as the organization grows
- Complies with PCI DSS Req. 8.3 and NIST IA-2 requirements

---

## Phase 1 — Audit, Scoping, and Tool Selection (Days 1–30)

**Objective:** Complete all preparation activities. No production changes to standard employee accounts.

### Tasks

| Task | Owner | Due | Deliverable |
|------|-------|-----|------------|
| Inventory all systems requiring MFA protection | IT Manager | Day 7 | Asset-to-authentication mapping |
| Identify legacy systems requiring hardware token support | IT Manager | Day 10 | Legacy compatibility assessment |
| Evaluate IAM vendor options (Duo vs. Entra ID) | IT Manager | Day 14 | Vendor evaluation matrix |
| Select and procure IAM platform | IT Manager | Day 21 | Signed contract / license |
| Draft MFA Enforcement Policy | IT Manager + Legal | Day 25 | Policy document (v1 draft) |
| Define MFA scope — which systems, which users, in what order | IT Manager | Day 30 | Enforcement scope document |

### Scope Definition

| System | MFA Required | Priority |
|--------|-------------|---------|
| E-commerce platform / payment database | Yes | Critical |
| Information Management System | Yes | Critical |
| Remote workstations | Yes | High |
| On-premises servers | Yes | High |
| Legacy systems | Yes (hardware tokens) | Medium |
| Internal email | Yes | Medium |

---

## Phase 2 — IT Team Pilot and Policy Sign-Off (Days 31–45)

**Objective:** Test the solution internally before broader rollout. Secure executive approval.

### Tasks

| Task | Owner | Due | Deliverable |
|------|-------|-----|------------|
| Activate MFA on IT team accounts only | IT Team | Day 33 | Pilot group active |
| Test MFA on on-premises server logins | IT Team | Day 37 | Test results documented |
| Test MFA on remote workstation logins | IT Team | Day 38 | Test results documented |
| Configure hardware security keys (YubiKey) for legacy systems | IT Manager | Day 40 | Legacy MFA functional |
| Document known issues and workarounds | IT Team | Day 42 | Issue log |
| Present pilot results and secure executive approval | IT Manager | Day 45 | Signed executive sign-off |

### Legacy System Approach

For systems incompatible with smartphone authenticator apps:
- **Option 1:** FIDO2 Hardware Security Keys (YubiKey 5 NFC)
- **Option 2:** Programmable TOTP tokens (e.g., SafeNet eToken)
- **Fallback:** Time-based OTP via SMS for non-sensitive systems only

---

## Phase 3 — User Training and Staged Rollout (Days 46–75)

**Objective:** Roll out MFA to all employees in controlled waves. Provide training and support.

### Communication

| Channel | Content | Date |
|---------|---------|------|
| Company-wide email | MFA announcement, purpose, and timeline | Day 46 |
| FAQ document | Step-by-step enrollment guide for authenticator app | Day 46 |
| IT support hours | Extended helpdesk for MFA setup questions | Days 46–75 |

### Wave Schedule

| Wave | User Group | Systems | Dates |
|------|-----------|---------|-------|
| **Wave 1** | E-commerce managers + Information Management System users | Payment database, IMS | Days 46–60 |
| **Wave 2** | All remote workers | Remote workstations, VPN | Days 61–75 |

### Training Requirements

All enrolled users must complete:
- 15-minute MFA onboarding module
- Enrollment confirmation within 5 business days of notification
- Backup authentication method configured (secondary email or hardware key)

---

## Phase 4 — Full Enforcement and Monitoring (Days 76–90)

**Objective:** Complete global enforcement. Monitor for anomalies. Close out the project.

### Tasks

| Task | Owner | Due | Deliverable |
|------|-------|-----|------------|
| Activate global conditional access policies | IT Manager | Day 76 | All non-MFA logins blocked |
| Lock out accounts not enrolled after grace period | IT Manager | Day 76 | Enforcement log |
| Dedicate hyper-care IT support for login issues | IT Team | Days 76–85 | Resolved ticket log |
| Distribute emergency hardware tokens to users who lost devices | IT Manager | Days 76–80 | Token issuance log |
| Connect MFA logs to monitoring tools | IT Team | Day 85 | Monitoring integration active |
| Flag and investigate failed MFA prompts > 3 in 5 minutes | IT Team | Day 86 | Alert ruleset documented |
| Final rollout report to executive leadership | IT Manager | Day 90 | Completion report |

### Enforcement Policy

As of Day 76:
- Any login to a Botium Toys asset without completed MFA enrollment is automatically blocked
- Emergency hardware token available from IT for users who lose their device
- MFA bypass requires IT Manager approval and is logged with justification

---

## Success Metrics

| KPI | Target |
|----|--------|
| MFA enrollment rate | 100% of in-scope users |
| Failed MFA attempts investigated | 100% within 24 hours |
| Support tickets resolved within SLA | ≥ 95% |
| Legacy systems protected with hardware tokens | 100% |
| Executive sign-off obtained | Day 45 |
| PCI DSS Req. 8.3 compliance achieved | Day 90 |

---

## Risk and Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Legacy system incompatibility | Medium | High | Hardware token fallback pre-configured in Phase 2 |
| Low user adoption | Medium | Medium | Training + hyper-care support period (Days 76–85) |
| IT resource overload | Medium | Medium | Phased rollout limits simultaneous support requests |
| Executive approval delayed | Low | High | Pilot data prepared as business case in Phase 2 |
| MFA bypass abuse | Low | High | Bypass requires IT Manager sign-off and is audit-logged |
