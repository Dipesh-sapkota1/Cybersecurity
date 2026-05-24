# Access Control Policy — Botium Toys (Recommended)

**Document Type:** Security Policy
**Status:** RECOMMENDED — Not Yet Implemented
**Framework Reference:** NIST SP 800-53 AC-3, AC-5, AC-6 | PCI DSS Req. 7 | GDPR Art. 25

---

## Purpose

Enforce least privilege and protect PII, SPII, and cardholder data from unauthorized access.

## Principles

1. **Least Privilege** — Minimum access required for job function
2. **Need to Know** — Access to sensitive data requires documented justification
3. **Separation of Duties** — High-risk actions require secondary review
4. **Default Deny** — Access denied by default; granted explicitly

## Access Control Requirements

| Requirement | Standard |
|------------|---------|
| Unique user IDs | Required for every employee and vendor |
| Shared accounts | Prohibited |
| Privileged accounts | Separate from standard; MFA required |
| Access reviews | Quarterly (privileged) / annually (standard) |
| Offboarding | Account disabled within 24 hours of departure |

## Data Access Tiers

| Tier | Data Type | Authorized Roles |
|------|----------|----------------|
| Tier 1 | Non-sensitive internal data | All employees |
| Tier 2 | Business operational data | Role-specific |
| Tier 3 | PII, SPII | Authorized roles with business need |
| Tier 4 | Cardholder data | PCI DSS authorized roles only |
