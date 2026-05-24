# Evidence Collection Standards

**Document Type:** Evidence Handling Standards
**Version:** 1.0
**Classification:** Internal

---

## Purpose

Define standards for collecting, storing, and managing audit evidence to maintain integrity, chain of custody, and compliance.

## Evidence Types

| Type | Examples |
|------|---------|
| Documentary | Policies, procedures, configuration screenshots |
| Technical | Log extracts, scan reports, configuration files |
| Observation | Walkthrough notes, interview records |

## Collection Procedures

1. Identify the control to be evidenced
2. Request evidence from the control owner
3. Validate that evidence directly supports the control assertion
4. Redact any PII, credentials, or sensitive data before storing
5. Hash the evidence file (SHA-256) to establish integrity
6. Log to the evidence register with ID, date, collector, and source

## Naming Convention

```
EVD-[YYYY]-[NNN]-[control-id]-[description].ext
Example: EVD-2024-001-AC-3-access-control-screenshot.png
```

## Retention

- Audit evidence: minimum 3 years
- PCI DSS evidence: minimum 1 year post-audit

## Storage

- Sensitive evidence must be stored in access-controlled systems
- Do not commit sensitive evidence to public repositories
- Reference by ID in documents only
