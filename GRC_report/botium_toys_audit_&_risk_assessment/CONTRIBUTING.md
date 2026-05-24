# Contributing Guidelines

Thank you for your interest in this project.

## Documentation Standards

- All documents use Markdown (`.md`) format
- File names are `kebab-case` (e.g., `risk-assessment-botium-toys.md`)
- Every document must include a header block with: Document Type, Classification, Version, and Prepared By

## Branch Naming

| Type | Format | Example |
|------|--------|---------|
| New document | `docs/topic-name` | `docs/incident-response-plan` |
| Update | `update/document-name` | `update/risk-register` |
| Fix | `fix/document-name` | `fix/compliance-matrix` |

## Commit Message Format

```
[type]: short description

Types: docs, fix, update, template, structure
Example: docs: add SOC 2 gap analysis
```

## Pull Request Requirements

- Reference the relevant issue number
- Include a brief description of what changed and why
- Ensure no PII or real credentials are included
- All new documents must follow the documentation standards in `docs/documentation-standards.md`
