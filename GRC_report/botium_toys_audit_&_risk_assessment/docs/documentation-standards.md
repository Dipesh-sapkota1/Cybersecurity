# Documentation Standards — v1.0

## File Naming

| Rule | Format | Example |
|------|--------|---------|
| All lowercase, hyphen-separated | `kebab-case.md` | `risk-assessment-botium.md` |
| Include context | `[type]-[topic].md` | `audit-report-botium-toys.md` |
| Templates suffixed with `-template` | | `risk-register-template.md` |

## Document Header Block (required on all documents)

```
**Document Type:** [Type]
**Classification:** [Public / Internal / Confidential]
**Version:** 1.0
**Prepared By:** [Name / Role]
```

## Classification Levels

| Level | Description |
|-------|-------------|
| Public | Safe for public GitHub; no sensitive data |
| Internal | Organizational use; no PII |
| Confidential | Contains findings; access-controlled |

> ⚠️ Do not store Confidential documents with real PII in public repositories.

## Markdown Standards

- ATX-style headers: `#`, `##`, `###`
- Pipe tables for tabular data
- Status icons: `✅` Compliant, `❌` Non-Compliant, `⚠️` Partial
- Fenced code blocks for config examples

## Version Control

| Version | Meaning |
|---------|---------|
| 1.0 | Initial publication |
| 1.x | Minor updates |
| 2.0 | Major revision |

## Evidence Handling

- Store sensitive evidence in access-controlled systems, not public repos
- Reference evidence by ID in documents (e.g., `EVD-2024-001`)
- Redact all PII from screenshots before committing

## Audit Trail

- All changes via pull request
- Use Issues to track findings and gaps
- Tag releases for milestone completions (e.g., `v1.0-initial-audit`)
