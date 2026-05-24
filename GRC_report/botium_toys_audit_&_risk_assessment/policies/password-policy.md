# Password Policy — Botium Toys (Recommended)

**Document Type:** Security Policy
**Status:** RECOMMENDED — Not Yet Implemented
**Framework Reference:** NIST SP 800-53 IA-5 | PCI DSS Req. 8.2, 8.6

---

## Purpose

Establish minimum password requirements to protect systems, customer data, and cardholder information from credential-based attacks.

## Scope

Applies to all employees, contractors, and vendors with access to any Botium Toys system.

## Password Requirements

| Requirement | Standard |
|------------|---------|
| Minimum length | 14 characters |
| Complexity | Uppercase, lowercase, number, special character |
| Prohibited | Dictionary words, username, sequential strings |
| Breached password check | Required (HaveIBeenPwned API) |
| Maximum age | 90 days (privileged) / 180 days (standard) |
| History | Last 12 passwords cannot be reused |
| Account lockout | 5 failed attempts → 30-minute lockout |

## MFA Requirements

MFA is required for:
- All remote access
- All access to cardholder data environments
- All privileged / administrator accounts

## Enforcement

- Centralized password management platform required
- Policy enforced technically, not by honor system
- Exceptions require IT Manager written approval and are time-limited
