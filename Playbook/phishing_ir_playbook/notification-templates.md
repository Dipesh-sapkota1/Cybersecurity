# Notification Templates
## NexaCore Technologies — Phishing Incident Communications

> These templates exist so that responders are not drafting messages under pressure during an active incident. Customize the bracketed fields for each incident. All **external communications require CISO and Legal approval** before sending.

---

## Template 1 — Notifying the Affected Employee

**Use when:** You are about to lock an employee's account or isolate their device.
**Send via:** Phone call or in-person. Do not use email.

---

*"Hi [Employee Name], this is [Your Name] from the NexaCore security team. I'm calling because we've identified a potential security issue related to your account and we need to take a few precautionary steps right now.*

*We're going to temporarily suspend your account access and take your computer offline briefly while we investigate. This is a standard protective measure and does not mean you've done anything wrong — phishing attacks are sophisticated and can fool anyone.*

*Here's what you need to know:*
- *Your account will be locked temporarily. We'll give you a temporary password and walk you through getting back in as soon as the investigation allows.*
- *If you're in the middle of important work, please save what you can right now.*
- *Please do not attempt to log in from another device until you hear from us.*

*Do you have any questions? I'll follow up with you directly as soon as I have more information."*

---

## Template 2 — Notifying the Employee's Manager

**Use when:** An employee's account or device is being taken offline (SEV-2 or higher).
**Send via:** Phone call.

---

*"Hi [Manager Name], this is [Your Name] from the NexaCore security team. I'm calling to let you know that we're currently investigating a potential security incident involving [Employee Name]'s account.*

*As a precaution, we've temporarily suspended their system access. This is standard procedure during an investigation and does not indicate wrongdoing on their part.*

*I wanted to make sure you're aware so you can plan for any coverage you may need. [Employee Name] has been informed and will be working with us to restore access as quickly as possible.*

*Please treat this as confidential for now — I'll provide updates as the situation develops. Please don't discuss this with other team members until we give the all-clear."*

---

## Template 3 — Company-Wide Phishing Alert

**Use when:** A phishing campaign has targeted multiple employees and all staff should be warned.
**Approved by:** CISO before sending.
**Send via:** Email from CISO, or Microsoft 365 organization-wide announcement.

---

**Subject:** ⚠️ Security Alert — Phishing Campaign Targeting NexaCore Employees

*Team,*

*The security team has identified a phishing email campaign currently targeting NexaCore employees. These emails are designed to look like [describe lure — e.g., "a Microsoft account verification request" / "an invoice from a known vendor"].*

*If you receive an email matching this description, do NOT click any links or open any attachments. Report it immediately using the Report Phishing button in Outlook or by forwarding it to security@nexacore.com.*

*What to look for:*
- *Sender: [Describe suspicious sender pattern — e.g., "emails appearing to come from microsoft-support@[random domain].com"]*
- *Subject line: [Describe common subject lines in this campaign]*
- *Content: [Describe the social engineering lure — e.g., "Claims your account will be suspended unless you verify your login"]*

*If you have already clicked a link or entered your credentials in response to one of these emails, contact the security team immediately at security@nexacore.com or call [security hotline number]. Do not wait.*

*The security team is actively investigating and has taken steps to block these emails. We will provide an update when the situation is resolved.*

*Thank you for your vigilance.*

*[CISO Name]*
*Chief Information Security Officer, NexaCore Technologies*

---

## Template 4 — Post-Incident Employee Notification (After Resolution)

**Use when:** An incident has been resolved and affected employees need to be informed of the outcome.
**Send via:** Email from IR Lead. Internal only.

---

**Subject:** Security Incident Update — NexaCore [Incident ID]

*Hi [Employee Name],*

*I'm writing to update you on the security incident we investigated involving your account on [Date].*

*What happened:*
*[Plain-language description of the incident — e.g., "A phishing email led to your Microsoft 365 credentials being entered on a fraudulent website. This gave an attacker temporary access to your account."]*

*What we did:*
*[Summarize containment and remediation actions taken]*

*What you need to do:*
- *Your password has been reset. Your temporary password is: [deliver this separately, not in the same email if possible]*
- *You will need to re-enroll your MFA device. Instructions: [link to guide]*
- *Your account will be under elevated monitoring for the next 30 days as a precaution*

*What this means going forward:*
*[Any specific guidance for this employee based on what was found]*

*If you notice anything unusual with your account or receive any suspicious follow-up emails, contact the security team immediately at security@nexacore.com.*

*Thank you for your cooperation throughout this process.*

*[IR Lead Name]*
*Incident Response Lead, NexaCore Security*

---

## Template 5 — External Client Notification (Data Breach)

**Use when:** Client personal or financial data was confirmed or suspected to have been accessed.
**REQUIRED: CISO and Legal must approve this message before it is sent.**
**Send via:** Formal email from CISO or Legal, with Legal in the loop.

---

**Subject:** Important Security Notice from NexaCore Technologies

*Dear [Client Contact Name],*

*We are writing to inform you of a security incident at NexaCore Technologies that may have affected data we process on your behalf.*

*What happened:*
*On [Date], NexaCore identified a phishing-based security incident that resulted in [brief, factual description of what occurred]. Our investigation determined that [describe scope of potential data access — be specific and factual; do not speculate].*

*What data was involved:*
*[List specific data types — e.g., "Account identifiers, transaction records for the period of [dates]"]*

*What we have done:*
*[Summarize containment and remediation steps taken]*

*What this means for you:*
*[Describe any actions the client should take, if any]*

*We take the security of your data extremely seriously and sincerely apologize for this incident. We are committed to providing you with full transparency throughout this process.*

*If you have questions or require further information, please contact [designated contact name and email].*

*Sincerely,*
*[CISO Name]*
*Chief Information Security Officer, NexaCore Technologies*
*[Contact information]*

---

*Notification Templates v1.0 | Maintained by IR Lead | Part of [Phishing IR Playbook](../playbook/phishing-playbook.md)*
