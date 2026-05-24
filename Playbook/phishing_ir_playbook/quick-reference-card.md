# ⚡ Phishing Incident — Quick Reference Card
## NexaCore Technologies | SOC Analyst Desk Reference

> This card is for **immediate use** when a phishing report comes in. For full procedures, see the [main playbook](phishing-playbook.md).

---

## Step 1 — Get the facts (First 15 minutes)

Ask the reporting user — via **phone or Teams**, not email:

- [ ] What is the sender name and email address?
- [ ] What is the subject line?
- [ ] Did you **open** the email?
- [ ] Did you **click** any link?
- [ ] Did you **enter** a username, password, or any other information?
- [ ] Did you **open** an attachment?
- [ ] Did anything unusual happen on your computer afterward?

**Open a ServiceNow ticket NOW** — before you do anything else.

---

## Step 2 — Classify Severity

| What happened | Severity | Your next move |
|---|---|---|
| Email reported, no interaction | SEV-4 Low | You handle it — quarantine & close |
| Email opened, nothing clicked | SEV-4 Low | You handle it — quarantine & monitor 48h |
| Link clicked, NO credentials entered | SEV-3 Medium | Escalate to IR Analyst within 4 hours |
| Credentials entered on any page | SEV-2 High | Call IR Lead NOW |
| Attachment opened / malware suspected | SEV-2 High | Call IR Lead NOW |
| Lateral movement or active breach | SEV-1 Critical | Page IR Lead AND CISO immediately |

> **When in doubt, go higher.** It's always better to escalate unnecessarily than to underclassify.

---

## Step 3 — Artifacts to Collect

Pull these from M365 Security Center / Outlook headers:

- [ ] Full sender address (display name + actual email)
- [ ] Reply-To address (if different from From)
- [ ] Sending server IP (use MXToolbox Header Analyzer)
- [ ] All URLs found in email body (copy, do NOT click)
- [ ] Attachment filename and hash (do NOT open)
- [ ] Timestamp of email delivery
- [ ] Full list of recipients at NexaCore

---

## Step 4 — Immediate Actions (SEV-4 / Containment)

**Quarantine email from all mailboxes:**
M365 Security Center → Threat Explorer → Search sender/subject → Select all → Soft Delete

**Block sender domain at email gateway:**
M365 Security Center → Tenant Allow/Block List → Add sender domain

**Analyze URLs safely (never open directly):**
→ [urlscan.io](https://urlscan.io) | [virustotal.com](https://virustotal.com) | [any.run](https://any.run)

---

## Escalation Contacts

| Who | When | How |
|---|---|---|
| IR Analyst | SEV-3 within 4 hours | Teams DM or call |
| IR Lead | SEV-2 within 1 hour | Call |
| IR Lead (after hours) | SEV-1 or SEV-2 | PagerDuty: nexacore-ir-oncall |
| CISO (after hours) | SEV-1 only | PagerDuty: nexacore-ciso-oncall |

**Report phishing email address:** security@nexacore.com
**Security incidents Teams channel:** #security-incidents

---

## What NOT to Do

- ❌ Do NOT click any links to "investigate" them — use sandboxes
- ❌ Do NOT open attachments on your workstation
- ❌ Do NOT email the reporting user from a potentially compromised account
- ❌ Do NOT wipe an endpoint before forensic imaging
- ❌ Do NOT tell other employees about the incident beyond those who need to know
- ❌ Do NOT contact external parties without CISO and Legal approval

---

*Quick Reference Card v1.0 | Full playbook: [phishing-playbook.md](phishing-playbook.md)*
