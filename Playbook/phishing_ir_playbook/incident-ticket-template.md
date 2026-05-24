# Phishing Incident Ticket Template
## NexaCore Technologies — ServiceNow | Security Incident

> Copy this template into ServiceNow when opening a phishing incident ticket. Fill in every field — blank fields create gaps in the record that affect post-incident review and compliance audits.

---

## SECTION 1 — Incident Identification

| Field | Value |
|---|---|
| **Ticket ID** | *(auto-assigned by ServiceNow)* |
| **Incident Title** | Phishing Incident — [Brief description e.g. "Credential harvest attempt targeting Finance team"] |
| **Date/Time Opened** | |
| **Opened By** | |
| **Current Severity** | SEV-1 / SEV-2 / SEV-3 / SEV-4 *(circle one)* |
| **Incident Status** | Open / In Progress / Contained / Closed |
| **Incident Owner** | |

---

## SECTION 2 — Reporter Information

| Field | Value |
|---|---|
| **Reported By** | |
| **Reporter's Department** | |
| **Report Method** | Outlook Report Phishing button / Email to security@ / SIEM alert / M365 Defender alert |
| **Date/Time of Report** | |
| **Date/Time of Original Email Delivery** | |

---

## SECTION 3 — Email Artifacts

| Field | Value |
|---|---|
| **Email Subject Line** | |
| **Sender Display Name** | |
| **Sender Email Address** | |
| **Reply-To Address** | *(if different from sender)* |
| **Sending Server IP** | |
| **All NexaCore Recipients** | *(list all)* |
| **URLs Found in Email** | *(list all — do not click)* |
| **Attachment Filename(s)** | |
| **Attachment Hash (SHA256)** | |

---

## SECTION 4 — User Interaction

| Field | Value |
|---|---|
| **Was the email opened?** | Yes / No |
| **Was a link clicked?** | Yes / No |
| **Were credentials entered?** | Yes / No — If yes, on what page? |
| **Was an attachment opened?** | Yes / No |
| **Any unusual system behavior reported?** | Yes / No — If yes, describe: |
| **Exact user statement (verbatim)** | *(quote what the user said when interviewed)* |

---

## SECTION 5 — Analysis Findings

| Field | Value |
|---|---|
| **URL Analysis Result** | *(URLScan.io / VirusTotal findings)* |
| **Attachment Analysis Result** | *(Any.run sandbox findings)* |
| **Azure AD Anomalous Logins?** | Yes / No — If yes, detail: |
| **Unauthorized Inbox Rules Found?** | Yes / No — If yes, detail: |
| **CrowdStrike Findings** | |
| **Splunk Correlation Findings** | *(other users affected?)* |
| **Confirmed Attack Type** | Credential harvest / Malware delivery / BEC / Other |
| **MITRE ATT&CK Technique** | T1566.001 / T1566.002 / T1566.003 |

---

## SECTION 6 — Containment Actions

| Action | Completed By | Timestamp |
|---|---|---|
| ServiceNow ticket created | | |
| Email quarantined from all mailboxes | | |
| Sender domain blocked at email gateway | | |
| Malicious URLs/IPs blocked at firewall | | |
| Endpoint isolated in CrowdStrike | | |
| Azure AD account disabled | | |
| Sessions and tokens revoked | | |
| Password reset completed | | |
| MFA re-enrollment completed | | |
| API keys rotated | | |

---

## SECTION 7 — Notifications Sent

| Recipient | Notified By | Method | Timestamp |
|---|---|---|---|
| Affected employee | | | |
| Employee's manager | | | |
| IR Lead | | | |
| CISO | | | |
| Legal | | | |
| Executive leadership | | | |
| External (clients/regulators) | | | |

---

## SECTION 8 — Evidence Log (Chain of Custody)

| Evidence Item | Collected By | Timestamp | Storage Location |
|---|---|---|---|
| Original email export (.eml) | | | |
| Email header analysis output | | | |
| Splunk log export | | | |
| Azure AD sign-in log export | | | |
| CrowdStrike telemetry export | | | |
| Endpoint disk image | | | |
| Sandbox analysis reports | | | |

---

## SECTION 9 — Timeline

*(List every significant event in chronological order)*

| Timestamp | Event |
|---|---|
| | Phishing email delivered to NexaCore mailbox(es) |
| | User interaction (click / credential entry / attachment open) |
| | Earliest attacker activity detected |
| | Incident detected by NexaCore |
| | Detection gap = *(subtract delivery from detection)* |
| | Ticket opened |
| | Escalation to IR |
| | Containment actions completed |
| | Eradication confirmed |
| | Systems/accounts returned to production |
| | Ticket closed |

---

## SECTION 10 — Closure

| Field | Value |
|---|---|
| **Date/Time Closed** | |
| **Closed By** | |
| **Final Severity** | SEV-1 / SEV-2 / SEV-3 / SEV-4 |
| **Root Cause** | |
| **Compromised?** | Yes — credentials stolen / Yes — malware executed / Yes — data accessed / No |
| **Post-Incident Review Scheduled?** | Yes — Date: _______ / Not required (SEV-4) |
| **Playbook Update Required?** | Yes / No |
| **Detection Rule Update Required?** | Yes / No |
| **Lessons Learned Summary** | *(1–3 sentences)* |

---

*Template v1.0 | Maintained by IR Lead | Part of [Phishing IR Playbook](../playbook/phishing-playbook.md)*
