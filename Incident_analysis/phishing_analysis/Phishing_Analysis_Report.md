# Phishing Email Analysis Report

---

## 1. Project Overview

This report documents my analysis of a phishing email sample as part of a cybersecurity capstone project. The goal was to apply basic email forensics techniques to identify signs of malicious intent in a real-world phishing sample.

The investigation covers the email headers, sender details, message content, embedded URLs, and indicators of compromise (IOCs). I also mapped the observed behaviors to relevant MITRE ATT&CK techniques.

**Scope:** This analysis is limited to static examination of the email sample. No dynamic malware analysis or live system testing was performed.

---

## 2. Sample Information

| Field             | Value                                                              |
| ----------------- | ------------------------------------------------------------------ |
| Email Sample      | sample-10.eml                                                      |
| Source Repository | GitHub – [rf-peixoto/phishing\_pot](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-10.eml) |
| SHA256            | 4fbf4c3d80aba156c59004c12c83ff53dd64c9cf7b7a6029e98fe1da0760783a  |
| Analysis Type     | Phishing Email Investigation                                       |

---

## 3. Executive Summary

This email impersonates the Microsoft account security team, claiming the recipient's account had an unusual sign-in attempt. The intent appears to be creating panic so the recipient clicks a suspicious tracking link or interacts with a `mailto:` link disguised as a reporting mechanism.

The email is a relatively unsophisticated phishing attempt. No credential harvesting page or malicious attachment was found. The tracked URL appears to have been taken down. Key red flags include a non-Microsoft sender domain, missing email authentication, and a `Reply-To` address pointing to a personal Gmail account.

---

## 4. Email Header Analysis

| Indicator      | Observation                                                              |
| -------------- | ------------------------------------------------------------------------ |
| Date           | 2023-09-08 11:32                                                         |
| From           | `no-reply@access-accsecurity.com` (not a Microsoft domain)              |
| To             | `phishing@pot` (generic recipient, likely a honeypot address)           |
| Reply-To       | `sotrecognizd@gmail.com` (personal Gmail, not Microsoft)                |
| Return-Path    | `bounce@thcultarfdes.co.uk` (unrelated third-party domain)              |
| Sender IP      | `89.144.44.2`                                                            |
| Resolved Host  | `r2.mscode.pl` (Polish hosting provider, MatHost.eu)                    |
| Message-ID     | `032672b4-77ca-42f8-a036-9711e91bd1f3@DB8EUR06FT032.eop-eur06.prod.protection.outlook.com` |

**Observations:**

The `From` domain (`access-accsecurity.com`) is not affiliated with Microsoft. The `Reply-To` field redirects responses to a Gmail address, which is unusual for any legitimate company security alert. The `Return-Path` points to an unrelated `.co.uk` domain. No SPF, DKIM, or DMARC authentication results are present in the available header data.

---

## 5. Sender Analysis

- **Display Name:** Microsoft account team
- **Sender Address:** `no-reply@access-accsecurity.com`
- **Reply-To:** `sotrecognizd@gmail.com`
- **Resolved Host:** `r2.mscode.pl`
- **Hosting Provider:** MatHost.eu (Poland), operated by Sebastian Stefanek

The sender is impersonating the Microsoft account team using a lookalike display name. The actual sending domain (`access-accsecurity.com`) has no connection to Microsoft. The domain name mimics security-related language (`accsecurity`) to appear credible at a glance.

The hosting infrastructure traces back to a generic Polish web host. Legitimate Microsoft security emails originate from `microsoft.com` or `accountprotection.microsoft.com` domains.

---

## 6. Content Analysis

- **Subject:** `Microsoft account unusual signin activity`
- **Body Theme:** Security alert warning the recipient of unusual sign-in activity on their Microsoft account

### Social Engineering Techniques

| Indicator                  | Detail                                                                 |
| -------------------------- | ---------------------------------------------------------------------- |
| Urgency / Fear             | Claims of unusual account activity to create panic                     |
| Impersonation              | Disguised as Microsoft account security team                           |
| False Reporting Mechanism  | `mailto:` link asking the user to "Report The User"                   |
| Vague Threat               | No specific account details provided (name, location, device)          |
| Generic Recipient          | No personalization; addressed to a honeypot inbox                     |

The email uses urgency as its main tactic. Real Microsoft security alerts typically include specific details like the device used, sign-in location, and timestamp. This email provides none of those, which is a sign it was sent in bulk without personalization.

The embedded `mailto:` link is also suspicious. Legitimate services never ask you to report suspicious activity by emailing them directly through a pre-filled mailto link.

---

## 7. URL Analysis

| URL                                                                              | Observation                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `hxxp[://]thebandalisty[.]com/track/o43062rdzGz18708448Gdrw1821750fYo33632dSjh176` | Defanged tracking URL; flagged as malicious on VirusTotal; returned bad gateway at time of analysis |
| `mailto:sotrecognizd@gmail.com` (via anchor tag)                                | Embedded `mailto:` link disguised as a reporting feature; routes responses to attacker-controlled Gmail |

The tracking URL appears to have been taken down or expired by the time of analysis, returning a bad gateway response. However, reputation services flagged the domain as malicious. The long randomized path in the URL is consistent with tracking links used in phishing campaigns to identify active targets.

The `mailto:` hyperlink is labeled "Report The User" but actually composes a pre-filled email to the attacker's Gmail address. This is an unusual self-reporting mechanism not used by legitimate services.

### URL Reputation Screenshot

> **Screenshot Placeholder**
>
> Insert URL reputation analysis screenshot here.
>
> Example: VirusTotal, URLVoid, Cisco Talos, or similar reputation service.

---

## 8. Indicators of Compromise (IOCs)

| IOC Type      | Value                                                              |
| ------------- | ------------------------------------------------------------------ |
| Email Address | `no-reply@access-accsecurity.com`                                  |
| Email Address | `sotrecognizd@gmail.com`                                           |
| Email Address | `bounce@thcultarfdes.co.uk` (Return-Path)                         |
| Domain        | `access-accsecurity.com`                                           |
| Domain        | `thcultarfdes.co.uk`                                               |
| Domain        | `thebandalisty.com`                                                |
| URL           | `hxxp[://]thebandalisty[.]com/track/o43062rdzGz18708448Gdrw1821750fYo33632dSjh176` |
| IP Address    | `89.144.44.2`                                                      |
| Subject       | `Microsoft account unusual signin activity`                        |
| Hash (SHA256) | `4fbf4c3d80aba156c59004c12c83ff53dd64c9cf7b7a6029e98fe1da0760783a` |

---

## 9. MITRE ATT\&CK Mapping

| Technique ID  | Technique Name                  | Description                                                                 |
| ------------- | ------------------------------- | --------------------------------------------------------------------------- |
| T1566.002     | Phishing: Spearphishing Link    | Email contains a suspicious tracking URL intended to lure the recipient     |
| T1566.001     | Phishing: Spearphishing via Service | Email impersonates a trusted service (Microsoft) to gain trust          |
| T1598.003     | Phishing for Information        | The `mailto:` link is designed to collect user responses/data              |
| T1204.001     | User Execution: Malicious Link  | Relies on user clicking the embedded URL to complete the attack             |

**Note:** These mappings are based on the observable behavior of the email. No confirmed post-exploitation activity was identified due to the URL being unavailable at the time of analysis.

---

## 10. Findings

- The sender domain (`access-accsecurity.com`) does not belong to Microsoft and appears designed to look security-related.
- The `Reply-To` address points to a personal Gmail account (`sotrecognizd@gmail.com`), which is not consistent with legitimate Microsoft communications.
- No email authentication (SPF/DKIM/DMARC) pass results were present in the available header data.
- The embedded tracking URL was flagged as malicious by reputation services but was inactive (bad gateway) at the time of analysis.
- The `mailto:` anchor link mimics a user reporting feature but routes responses directly to the attacker.
- The email body uses urgency and fear of account compromise to push the recipient to interact.
- No malicious attachments or credential harvesting pages were identified, suggesting this may be a reconnaissance or tracking campaign.
- The sending infrastructure traces to a shared Polish hosting provider, not Microsoft.

---

## 11. Conclusion

Analyzing this phishing sample gave me practical experience applying email forensics concepts I had previously only studied theoretically. Walking through the headers, sender details, URLs, and content highlighted how attackers combine technical deception (fake domains, mismatched headers) with psychological pressure (urgency, impersonation) to manipulate recipients.

Even though this particular sample appears unsophisticated and the malicious URL was already offline, it still demonstrates realistic techniques used in phishing campaigns. Recognizing these patterns early is an important skill for anyone working in a defensive security role.

This project reinforced that phishing remains one of the most common entry points for attackers, and that careful email inspection — even without advanced tooling — can surface clear indicators of malicious intent.

---

## 12. References

- **Email Sample Source:** [rf-peixoto/phishing\_pot – sample-10.eml](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-10.eml)
- **MITRE ATT\&CK Framework:** [https://attack.mitre.org](https://attack.mitre.org)
- **VirusTotal (URL Reputation):** [https://www.virustotal.com](https://www.virustotal.com)
- **URLVoid (Domain Reputation):** [https://www.urlvoid.com](https://www.urlvoid.com)
- **Cisco Talos Intelligence:** [https://talosintelligence.com](https://talosintelligence.com)
- **Microsoft Safety Tips (Phishing Awareness):** [https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44](https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44)
