# Email Phishing Incident Response Playbook
## NexaCore Technologies — Security Operations

---

| Field | Detail |
|---|---|
| **Document Title** | Email Phishing Incident Response Playbook |
| **Version** | 1.0 |
| **Classification** | Internal Use Only |
| **Author** | Security Operations Team |
| **Created** | May 2026 |
| **Last Reviewed** | May 2026 |
| **Next Review** | August 2026 |
| **Owner** | CISO |
| **Framework** | NIST SP 800-61 Rev. 2 |

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Scope](#2-scope)
3. [Threat Overview](#3-threat-overview)
4. [Roles and Responsibilities](#4-roles-and-responsibilities)
5. [Tools and Resources](#5-tools-and-resources)
6. [Severity Classification](#6-severity-classification)
7. [Phase 1 — Preparation](#7-phase-1--preparation)
8. [Phase 2 — Detection and Analysis](#8-phase-2--detection-and-analysis)
9. [Phase 3 — Containment and Eradication](#9-phase-3--containment-and-eradication)
10. [Phase 4 — Recovery](#10-phase-4--recovery)
11. [Phase 5 — Post-Incident Activity](#11-phase-5--post-incident-activity)
12. [Escalation Path](#12-escalation-path)
13. [Communication Plan](#13-communication-plan)
14. [Evidence Handling and Chain of Custody](#14-evidence-handling-and-chain-of-custody)
15. [Compliance Notification Requirements](#15-compliance-notification-requirements)

---

## 1. Purpose

This playbook defines the standard operating procedure for identifying, analyzing, containing, and recovering from email phishing incidents at NexaCore Technologies.

Its purpose is to:
- Reduce response time by eliminating guesswork during an active incident
- Ensure consistent, repeatable response actions across all security team members
- Preserve forensic evidence for legal and compliance purposes
- Meet NexaCore's obligations under SOC 2 Type II, PCI-DSS, and GDPR

This document is **operational** — it is written to be followed by a responder in real time, not read as background material.

---

## 2. Scope

**This playbook applies to:**
- All email phishing threats targeting NexaCore employees via Microsoft 365 (Outlook)
- Phishing variants including: credential harvesting, malware delivery, Business Email Compromise (BEC), and spear phishing targeting executives
- All NexaCore endpoints connected to corporate Azure AD, regardless of physical location (office or remote)

**This playbook does NOT cover:**
- SMS phishing (smishing) — see Smishing Playbook v1.0
- Voice phishing (vishing) — see Vishing Playbook v1.0
- Phishing attacks targeting NexaCore's clients (handled by Client Incident Response team)

**Environment in scope:**
- Email platform: Microsoft 365 / Exchange Online
- Identity provider: Azure Active Directory
- Endpoints: Windows 11 corporate devices managed via Intune
- SIEM: Splunk Enterprise Security
- EDR: CrowdStrike Falcon
- Ticketing: ServiceNow

---

## 3. Threat Overview

### What is Email Phishing?

Email phishing is a social engineering attack where a threat actor sends fraudulent emails that appear to originate from trusted sources — such as Microsoft, a bank, a vendor, or a NexaCore executive — to trick recipients into revealing credentials, clicking malicious links, or opening malicious attachments.

### Why NexaCore is a Target

NexaCore processes financial transaction data for 400+ enterprise clients. Successful phishing against NexaCore employees can give attackers:
- Access to Azure AD credentials, enabling login to client-facing portals
- Access to internal financial systems containing PCI-scoped payment data
- The ability to impersonate NexaCore to target its clients (supply chain phishing)

### Attack Lifecycle (MITRE ATT&CK: T1566)

```
[1] DELIVERY       Attacker sends phishing email to NexaCore employee
        ↓
[2] INTERACTION    Victim opens email; clicks link or opens attachment
        ↓
[3] EXPLOITATION   Credential harvest via fake login page
                   OR malware execution via malicious attachment/macro
        ↓
[4] ACTION         Attacker uses stolen credentials or malware
                   to access systems, move laterally, or exfiltrate data
```

### Common Phishing Scenarios at NexaCore

| Scenario | Description | Risk Level |
|---|---|---|
| Credential harvesting | Fake Microsoft 365 login page steals Azure AD credentials | Critical |
| BEC — CEO fraud | Attacker impersonates CEO to request wire transfer or gift cards | High |
| Malware attachment | Malicious Office macro or PDF dropper installs ransomware or RAT | Critical |
| Vendor impersonation | Email appears to come from trusted vendor requesting payment change | High |
| IT helpdesk lure | Fake IT email asks employee to "verify" their account credentials | High |

---

## 4. Roles and Responsibilities

### Security Team Structure at NexaCore

```
CISO (Chief Information Security Officer)
│
├── IR Lead (Incident Response Lead)
│     └── IR Analyst x2
│
├── SOC (Security Operations Center)
│     └── SOC Analyst x3 (Tier 1, Tier 2, Tier 3)
│
└── IT Security Admin x1
```

### RACI Matrix

R = Responsible | A = Accountable | C = Consulted | I = Informed

| Action | SOC Analyst | IR Analyst | IR Lead | IT Sec Admin | CISO | Legal/HR |
|---|---|---|---|---|---|---|
| Receive and triage phishing report | R | — | I | — | — | — |
| Create incident ticket | R | — | — | — | — | — |
| Perform initial email analysis | R | C | — | — | — | — |
| Escalate to IR team | R | — | A | — | I | — |
| Conduct in-depth investigation | C | R | A | — | I | — |
| Quarantine email from all mailboxes | — | R | A | C | I | — |
| Isolate compromised endpoint | — | C | A | R | I | — |
| Reset compromised credentials | — | C | A | R | I | — |
| Determine breach notification need | C | C | R | — | A | C |
| Notify affected employees | — | — | R | — | A | C |
| External/regulatory notification | — | — | C | — | A | R |
| Conduct post-incident review | C | R | A | C | I | — |
| Update playbook | — | R | A | — | I | — |

### Role Descriptions

**SOC Analyst (Tier 1)**
First responder. Receives phishing reports via SIEM alert or user ticket. Performs initial triage and determines whether to close as false positive or escalate.

**IR Analyst**
Takes ownership of confirmed incidents. Conducts deep technical investigation, coordinates containment, and manages evidence collection.

**IR Lead**
Manages the overall incident response process. Makes escalation decisions. Approves containment actions that affect business operations. Serves as point of contact for CISO and Legal.

**IT Security Admin**
Executes technical containment actions on infrastructure — endpoint isolation via CrowdStrike, account lockouts in Azure AD, mail gateway rule updates.

**CISO**
Accountable for all decisions with regulatory, legal, or business impact. Approves external notifications. Briefs executive leadership.

**Legal / HR**
Consulted when an employee is suspected of being a victim of BEC, when external parties must be notified, or when regulatory reporting is required.

---

## 5. Tools and Resources

| Function | Tool | Access |
|---|---|---|
| SIEM / Alert detection | Splunk Enterprise Security | SOC workstations, SOC portal |
| EDR / Endpoint isolation | CrowdStrike Falcon | CrowdStrike console |
| Email analysis / quarantine | Microsoft Defender for Office 365 | M365 Security Center |
| Identity & access management | Azure Active Directory | Azure Admin Portal |
| URL sandbox analysis | Any.run / URLScan.io | any.run / urlscan.io (web) |
| File sandbox analysis | Any.run / VirusTotal | any.run / virustotal.com |
| Incident ticketing | ServiceNow | ServiceNow portal |
| Email header analysis | MXToolbox Header Analyzer | mxtoolbox.com/EmailHeaders |
| Threat intelligence | MITRE ATT&CK | attack.mitre.org |
| Internal communication | Microsoft Teams — #security-incidents channel | Teams |

---

## 6. Severity Classification

Every phishing incident must be classified before a response path is chosen. Classification determines response urgency, escalation, and notification requirements.

| Severity | Criteria | Response SLA | Escalate To |
|---|---|---|---|
| **SEV-1 Critical** | Active breach confirmed; lateral movement or data exfiltration detected; ransomware executing; multiple accounts compromised | Immediate — page IR Lead and CISO now | IR Lead, CISO, Legal |
| **SEV-2 High** | Credentials confirmed entered on phishing page; malware executed on endpoint; BEC wire transfer attempted | 1 hour | IR Lead, CISO |
| **SEV-3 Medium** | User clicked phishing link; no credential entry confirmed; suspicious attachment opened but no execution confirmed | 4 hours | IR Analyst |
| **SEV-4 Low** | Phishing email reported by user; no interaction (no click, no open) | 24 hours | SOC Analyst handles |

> **Default to higher severity when uncertain.** It is always better to escalate a SEV-3 and stand down than to underclassify a SEV-1 and respond too slowly.

---

## 7. Phase 1 — Preparation

Preparation is everything that must exist *before* an incident occurs. This phase is owned by the IR Lead and reviewed quarterly.

### 7.1 Detection Infrastructure

Ensure the following Splunk detection rules are active and tested:

- [ ] Alert on emails with mismatched Reply-To and From domains
- [ ] Alert on emails containing known phishing keywords (invoice, urgent, verify, suspended)
- [ ] Alert on login attempts from new geographic locations after clicking an external link
- [ ] Alert on mass email deletion events in Exchange (post-compromise cleanup behavior)
- [ ] Alert on creation of new inbox rules forwarding email externally

### 7.2 Access and Tooling Readiness

- [ ] All SOC analysts have active, MFA-enrolled access to Splunk, M365 Security Center, and CrowdStrike
- [ ] IR Analysts have admin rights to quarantine emails in M365 and isolate endpoints in CrowdStrike
- [ ] IT Security Admin has break-glass access to Azure AD for emergency account lockouts
- [ ] ServiceNow phishing incident template is current and accessible

### 7.3 Employee Awareness

- [ ] All NexaCore employees have completed phishing awareness training (annual minimum)
- [ ] Phishing simulation campaigns run quarterly; results reviewed by IR Lead
- [ ] Employees know how to report suspicious emails: **Report Phishing button in Outlook** or email `security@nexacore.com`
- [ ] All employees know NOT to click links in suspicious emails, even to investigate themselves

### 7.4 Playbook and Contact List Currency

- [ ] This playbook has been reviewed in the last 90 days
- [ ] On-call rotation for IR Lead and CISO is current and posted in Teams #security-incidents
- [ ] Legal and HR contacts are documented and up to date (see Section 13)

---

## 8. Phase 2 — Detection and Analysis

### 8.1 How Phishing Incidents Are Detected at NexaCore

| Detection Source | Description |
|---|---|
| User report | Employee clicks Report Phishing in Outlook or emails security@nexacore.com |
| Splunk SIEM alert | Automated rule fires based on email or login behavior |
| M365 Defender alert | Microsoft's built-in threat detection flags email or attachment |
| SOC proactive hunt | Analyst identifies suspicious pattern during threat hunting |

### 8.2 Initial Triage (SOC Analyst — Tier 1)

**Time target: Within 15 minutes of alert or report**

**Step 1 — Open a ServiceNow ticket immediately.**
Do this before investigation begins. Use the Phishing Incident template.
Ticket fields to populate now: Reporter name, timestamp, email subject line, initial severity guess (update later).

**Step 2 — Collect basic email artifacts.**
Retrieve the following from M365 Security Center or directly from the reported email:

- Full sender address (display name AND actual email address — these are often different in phishing)
- Reply-To address (if different from From)
- Return-Path address
- Sending server IP address (from email headers — use MXToolbox Header Analyzer)
- Email subject line
- Timestamp of delivery
- List of all recipients at NexaCore who received this email
- Any URLs in the email body (do NOT click them)
- Any attachments (do NOT open them)

**Step 3 — Determine user interaction.**

Ask the reporting user directly (via Teams or phone — not email):
- Did you click any link in the email?
- Did you open any attachment?
- Did you enter any username, password, or other information on any page?
- Did you notice anything unusual on your computer afterward (slow performance, unexpected popups, programs launching)?

> **This single conversation determines your response path.** Document the answers word-for-word in the ticket.

---

### 8.3 Response Path Decision

Based on triage findings, choose your path:

```
Was the phishing email opened?
│
├── NO (email sits unopened or was deleted without opening)
│     → SEV-4 Low
│     → Quarantine email from all mailboxes (Section 9.1)
│     → Close ticket as contained. No further action.
│
└── YES — Was any link clicked or attachment opened?
      │
      ├── NO (opened but no interaction)
      │     → SEV-4 Low
      │     → Quarantine email. Monitor mailbox for 48 hours.
      │
      └── YES — Were credentials entered OR was attachment opened/executed?
            │
            ├── LINK CLICKED, NO CREDENTIALS ENTERED
            │     → SEV-3 Medium
            │     → Escalate to IR Analyst
            │     → Proceed to Section 8.4 (URL Analysis)
            │
            ├── CREDENTIALS ENTERED
            │     → SEV-2 High → Escalate to IR Lead immediately
            │     → Proceed to Section 8.5 (Account Compromise Investigation)
            │
            └── ATTACHMENT OPENED / MALWARE SUSPECTED
                  → SEV-2 High or SEV-1 Critical
                  → Escalate to IR Lead immediately, notify CISO
                  → Proceed to Section 8.6 (Malware Investigation)
```

---

### 8.4 URL Analysis (IR Analyst)

For all incidents where a link was clicked:

**Step 1 — Analyze the URL safely (never open in a browser directly).**

Submit the URL to:
- URLScan.io — for a screenshot and network behavior analysis
- VirusTotal — for multi-engine reputation check
- Any.run — for interactive sandbox if the URL delivers a file

**Step 2 — Document what the URL resolves to:**
- Is it a credential harvesting page (fake Microsoft login, etc.)?
- Does it redirect to a file download?
- Is it already taken down (may indicate a fast-burning campaign)?

**Step 3 — Check Splunk for other users who clicked the same URL.**

```
Search: index=proxy_logs url="[suspicious URL]"
```

If more than one user clicked, immediately escalate severity and notify IR Lead.

---

### 8.5 Account Compromise Investigation (IR Analyst)

For all incidents where credentials were entered:

**Step 1 — Pull Azure AD sign-in logs immediately.**

In Azure AD Portal → Sign-in logs → filter by affected user → look for:
- Logins from new/unknown IP addresses
- Logins from unexpected geographic locations
- Logins at unusual times
- Token refresh activity (attacker reusing session token after credential theft)

**Step 2 — Check for post-compromise activity in M365.**

In M365 Security Center:
- Were any new inbox forwarding rules created?
- Were large volumes of email read or deleted?
- Were any new OAuth apps authorized?
- Were any external file shares created in SharePoint or OneDrive?

**Step 3 — Check for lateral movement in Splunk.**

Search for authentication events from the compromised account accessing systems they do not normally access.

**Step 4 — Determine scope.**

Is this limited to one account, or has the attacker used these credentials to access other systems? If lateral movement is confirmed → immediately escalate to SEV-1 Critical.

---

### 8.6 Malware Investigation (IR Analyst + IT Security Admin)

For all incidents where a malicious attachment was opened or malware is suspected:

**Step 1 — Pull CrowdStrike Falcon telemetry for the affected endpoint.**

Look for:
- Process execution events at or after the time the attachment was opened
- Suspicious child processes (e.g., Office spawning PowerShell, cmd.exe)
- New persistence mechanisms (registry run keys, scheduled tasks)
- Network connections to external IPs made by unusual processes
- File write events in system directories

**Step 2 — Submit the attachment to Any.run sandbox.**

Do not open on a live machine. Upload the file hash or attachment to Any.run for safe detonation and behavioral analysis.

**Step 3 — Determine scope.**

Has the malware spread to other endpoints via network shares or lateral movement? Check Splunk for similar process execution events across other endpoints.

---

## 9. Phase 3 — Containment and Eradication

### 9.1 Email Containment (All Severity Levels)

**Action: Quarantine the phishing email from all NexaCore mailboxes.**

Performed by: IR Analyst via Microsoft Defender for Office 365

In M365 Security Center → Threat Explorer → Search by sender address or subject line → Select all matching emails → Soft delete (moves to quarantine, recoverable) or Hard delete (for confirmed malicious content).

Document: Number of mailboxes affected, timestamp of quarantine action.

**Action: Block the sending domain and IP at the email gateway.**

In M365 Security Center → Tenant Allow/Block List → Add sender domain and IP to block list.

---

### 9.2 Endpoint Isolation (SEV-2 and SEV-1)

**Action: Isolate the compromised endpoint from the network.**

Performed by: IT Security Admin via CrowdStrike Falcon

In CrowdStrike Falcon console → Endpoint Management → Select affected device → Network Containment → Contain.

> Network containment cuts the endpoint off from all network access **except** the CrowdStrike management channel — this preserves the ability to investigate and reverse the action remotely.

Notify the affected employee's manager that their device will be temporarily unavailable. Arrange a loaner device if needed to maintain business continuity.

**Do NOT wipe or reimage the endpoint yet** — the disk is forensic evidence and must be preserved until imaging is complete.

---

### 9.3 Account Containment (SEV-2 and SEV-1)

**Action: Disable the compromised Azure AD account.**

Performed by: IT Security Admin via Azure AD Portal

Azure AD Portal → Users → Select affected user → Disable account.

Notify the user and their manager immediately via phone. Do not use email (the mailbox may be under attacker control).

**Action: Revoke all active sessions and tokens.**

Azure AD Portal → Users → Select affected user → Revoke sessions.

This invalidates all current OAuth tokens and forces re-authentication on all devices and applications.

**Action: Reset the compromised password.**

Do not allow the user to choose their own reset until the investigation is complete — they may be under active social engineering. IT Security Admin sets a temporary password and delivers it via phone or in person.

**Action: Revoke and rotate any API keys or service account credentials** associated with the compromised account.

---

### 9.4 Network Containment (SEV-1 Critical only)

**Action: Block malicious domains and IPs at the firewall.**

Performed by: IT Security Admin

Block all external domains and IPs identified in the investigation at the perimeter firewall. Document each block with justification.

**Action: Disable external sharing** in SharePoint and OneDrive if data exfiltration is suspected, pending investigation.

---

### 9.5 Eradication

After containment is confirmed:

- [ ] Remove malware from isolated endpoint using CrowdStrike Falcon's real-time response
- [ ] Delete any persistence mechanisms identified (registry keys, scheduled tasks, startup entries)
- [ ] Remove any unauthorized inbox rules or email forwarding rules from affected mailboxes
- [ ] Remove any unauthorized OAuth applications authorized by the compromised account
- [ ] Audit and remove any accounts or backdoors created by the attacker during the compromise window
- [ ] Verify eradication with a second analyst — do not mark this step complete alone

---

## 10. Phase 4 — Recovery

### 10.1 System Recovery

**Endpoint restoration:**
- If malware was confirmed: Wipe and reimage the endpoint from a known-good image. Do not restore from a backup taken after the initial compromise timestamp.
- If no malware execution confirmed: Release from CrowdStrike network containment after investigation is complete and eradication is verified.

**Account restoration:**
- Re-enable the Azure AD account only after password reset and MFA re-enrollment are confirmed
- Require the user to enroll a new MFA method (the old method may have been compromised)
- Restore access to systems and data on a need-to-know basis — do not restore full access at once

### 10.2 Verification Before Returning to Production

Before returning any system or account to production use, the IR Analyst must confirm:

- [ ] No indicators of compromise remain on the endpoint (CrowdStrike clean scan)
- [ ] No unauthorized forwarding rules or OAuth apps remain in the mailbox
- [ ] Azure AD sign-in logs show no unexpected activity since remediation
- [ ] Splunk shows no residual C2 (command and control) traffic from the endpoint
- [ ] All identified malicious IPs and domains remain blocked

### 10.3 User Communication Post-Recovery

Before the user's access is restored, the IR Lead or their delegate must meet with the user (in person or video call) to:
- Explain what happened and what was found
- Confirm the user understands how the phishing attack worked
- Provide targeted awareness coaching on the specific tactic used
- Set expectations for monitoring (their account will be under elevated monitoring for 30 days)

---

## 11. Phase 5 — Post-Incident Activity

### 11.1 Incident Timeline Reconstruction

The IR Analyst must reconstruct a complete timeline of the incident, from initial delivery to full remediation. The timeline must include:

- Timestamp of phishing email delivery
- Timestamp of user interaction (click, credential entry, attachment open)
- Timestamp of attacker activity (any unauthorized logins, data access, lateral movement)
- Timestamp of detection
- Timestamp of each containment action
- Timestamp of full remediation

**Detection Gap = Timestamp of first attacker action − Timestamp of detection**

This metric is reported to the CISO and tracked over time.

### 11.2 Post-Incident Review Meeting

A post-incident review meeting must be held within 5 business days of incident closure for all SEV-1, SEV-2, and SEV-3 incidents.

Attendees: IR Analyst, IR Lead, SOC Lead, IT Security Admin, CISO (for SEV-1)

Agenda:
1. Incident timeline walkthrough
2. What detection mechanisms caught it — or why they didn't
3. What worked in the response
4. What was slower or harder than it should have been
5. Specific action items with owners and due dates

### 11.3 Playbook and Control Updates

Every post-incident review must produce at least one of the following:

- A new or updated Splunk detection rule
- An update to this playbook
- A new employee awareness training topic
- A change to email gateway policy
- A technical control improvement (e.g., conditional access rule, MFA policy update)

Updates to this playbook require IR Lead approval and are version-controlled in this repository.

### 11.4 Phishing Simulation Follow-up

If the incident revealed that a significant number of employees failed to recognize the phishing attempt, the IR Lead will coordinate with HR to schedule targeted phishing simulation training for the affected department within 30 days.

---

## 12. Escalation Path

```
Phishing email reported
        ↓
SOC Analyst (Tier 1) — Initial triage
        ↓
SEV-4 Low? → SOC Analyst handles and closes
        ↓
SEV-3 Medium? → Escalate to IR Analyst within 4 hours
        ↓
SEV-2 High? → Escalate to IR Lead within 1 hour
        ↓
SEV-1 Critical? → Page IR Lead and CISO immediately (24/7)
                   Notify Legal if data breach is suspected
```

### After-Hours Escalation

| Role | Contact Method |
|---|---|
| IR Lead on-call | PagerDuty — nexacore-ir-oncall rotation |
| CISO | PagerDuty — nexacore-ciso-oncall rotation |
| Legal | On-call contact listed in Teams #security-incidents (pinned) |

For SEV-1 incidents, do not wait for business hours. Page immediately.

---

## 13. Communication Plan

### Internal Communication

| Audience | When | Channel | Who Sends |
|---|---|---|---|
| Affected employee's manager | Within 1 hour of SEV-2/SEV-1 confirmation | Phone call | IR Lead |
| Affected employee | When account/device is being locked | Phone call | IT Security Admin |
| All NexaCore employees (if campaign is widespread) | After initial containment | Email from CISO | CISO |
| Executive leadership | SEV-1 only, within 2 hours | Briefing from CISO | CISO |

### External Communication

External communication **requires CISO and Legal approval** before any message is sent.

| Audience | When | Trigger |
|---|---|---|
| Affected clients | Per GDPR/contractual obligation | Client data confirmed or suspected accessed |
| Regulators (GDPR supervisory authority) | Within 72 hours of confirmed personal data breach | EU client personal data involved |
| PCI-DSS QSA | Per PCI-DSS breach notification requirements | Payment card data involved |
| Law enforcement | At Legal's direction | Suspected criminal activity, extortion |

---

## 14. Evidence Handling and Chain of Custody

All evidence collected during an incident must be handled in a way that preserves its integrity for potential legal proceedings.

### Evidence to Collect and Preserve

| Evidence Type | Collection Method | Storage Location |
|---|---|---|
| Original phishing email (with headers) | Export as .eml from M365 | Secure evidence folder in SharePoint (IR team only) |
| Email header analysis output | Screenshot or text export from MXToolbox | ServiceNow ticket attachment |
| Splunk alert and log exports | Export relevant log data as CSV | Secure evidence folder |
| CrowdStrike telemetry | Export process tree and event data from Falcon | Secure evidence folder |
| Azure AD sign-in logs | Export CSV from Azure AD Portal | Secure evidence folder |
| Disk image of compromised endpoint | Forensic image via CrowdStrike RTR | Encrypted storage, IR Lead access only |
| URLScan / sandbox reports | Save PDF or screenshot | ServiceNow ticket attachment |

### Chain of Custody Requirements

- All evidence must be logged in the ServiceNow incident ticket with: what was collected, when, and by whom
- Evidence must not be altered after collection — work from copies
- Access to the secure evidence folder is restricted to IR team members
- If law enforcement involvement is anticipated, contact Legal before touching any additional evidence

---

## 15. Compliance Notification Requirements

NexaCore operates under the following regulatory frameworks. The IR Lead is responsible for triggering notifications — the CISO is accountable for approving them.

### GDPR (Applies to EU client data)

| Requirement | Detail |
|---|---|
| Notification trigger | Personal data of EU individuals confirmed or likely accessed by unauthorized party |
| Notify whom | Relevant EU supervisory authority (e.g., ICO if UK clients affected) |
| Deadline | **Within 72 hours** of becoming aware of the breach |
| Owner | CISO, with Legal |

### PCI-DSS (Applies to payment card data)

| Requirement | Detail |
|---|---|
| Notification trigger | Payment card data confirmed or suspected accessed |
| Notify whom | Card brands (Visa, Mastercard) and acquiring bank |
| Deadline | **Immediately** upon confirmation of compromise |
| Owner | CISO, with Legal and Finance |

### SOC 2 Type II

| Requirement | Detail |
|---|---|
| Documentation requirement | All security incidents must be documented and available for auditor review |
| Retention | Incident records retained for minimum 1 year |
| Owner | IR Lead ensures ServiceNow records are complete and accurate |

---

*End of Playbook — Version 1.0*

*This is a living document. Submit updates via pull request to this repository. All changes require IR Lead review.*
