# References and Further Reading

## Frameworks and Standards

| Resource | Description | Link |
|---|---|---|
| **NIST SP 800-61 Rev. 2** | Computer Security Incident Handling Guide — the primary framework used to structure this playbook | [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) |
| **MITRE ATT&CK — T1566** | Phishing technique documentation with real-world sub-techniques and adversary examples | [attack.mitre.org/techniques/T1566](https://attack.mitre.org/techniques/T1566/) |
| **MITRE ATT&CK — Initial Access** | Full Initial Access tactic overview showing how phishing fits into the attack lifecycle | [attack.mitre.org/tactics/TA0001](https://attack.mitre.org/tactics/TA0001/) |
| **CISA Phishing Guidance** | US government guidance on phishing prevention and response | [cisa.gov/phishing](https://www.cisa.gov/phishing) |
| **ISO/IEC 27035** | International standard for information security incident management | iso.org |

---

## Compliance References

| Regulation | Relevance to This Playbook | Key Resource |
|---|---|---|
| **GDPR (EU) 2016/679** | Article 33 mandates notification to supervisory authority within 72 hours of confirmed personal data breach | [gdpr-info.eu](https://gdpr-info.eu/art-33-gdpr/) |
| **PCI-DSS v4.0** | Requirement 12.10 — incident response plan requirements for cardholder data environments | [pcisecuritystandards.org](https://www.pcisecuritystandards.org) |
| **SOC 2 Trust Services Criteria** | CC7.3 — organizations must have procedures to respond to security incidents | [aicpa.org](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/sorhome.html) |

---

## Tooling Documentation

| Tool | Purpose in Playbook | Documentation |
|---|---|---|
| **Microsoft Defender for Office 365** | Email quarantine, Threat Explorer, Tenant Allow/Block List | [learn.microsoft.com/defender-office-365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/) |
| **Microsoft Azure AD Sign-in Logs** | Detecting unauthorized logins post-compromise | [learn.microsoft.com/azure/active-directory](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins) |
| **CrowdStrike Falcon** | Endpoint detection, network containment, real-time response | [falcon.crowdstrike.com/documentation](https://falcon.crowdstrike.com) |
| **Splunk Enterprise Security** | SIEM alerting, log correlation, threat hunting | [docs.splunk.com](https://docs.splunk.com/Documentation/ES) |
| **URLScan.io** | Safe URL analysis and screenshot of suspicious pages | [urlscan.io](https://urlscan.io) |
| **VirusTotal** | Multi-engine reputation check for URLs, IPs, and file hashes | [virustotal.com](https://www.virustotal.com) |
| **Any.run** | Interactive sandbox for safe detonation of attachments and URLs | [any.run](https://any.run) |
| **MXToolbox Header Analyzer** | Email header parsing for sender IP and routing analysis | [mxtoolbox.com/EmailHeaders](https://mxtoolbox.com/EmailHeaders.aspx) |

---

## Further Reading

### Books

- *The Practice of Network Security Monitoring* — Richard Bejtlich
- *Blue Team Handbook: Incident Response Edition* — Don Murdoch
- *Intelligence-Driven Incident Response* — Scott Roberts & Rebekah Brown

### Free Online Resources

| Resource | Description |
|---|---|
| [SANS Internet Storm Center](https://isc.sans.edu) | Daily threat intelligence and phishing campaign reports |
| [PhishTank](https://www.phishtank.com) | Community-maintained database of verified phishing URLs |
| [OpenPhish](https://openphish.com) | Free phishing intelligence feed |
| [Have I Been Pwned](https://haveibeenpwned.com) | Check if NexaCore email domains appear in known breach datasets |
| [Google Transparency Report — Safe Browsing](https://transparencyreport.google.com/safe-browsing/search) | URL reputation check for suspected phishing pages |

### Certifications Relevant to Incident Response

| Certification | Body | Relevance |
|---|---|---|
| CompTIA Security+ | CompTIA | Foundation — covers incident response concepts |
| CompTIA CySA+ | CompTIA | Intermediate — threat detection and response |
| GIAC GCIH | GIAC/SANS | Advanced — hands-on incident handling |
| EC-Council CEH | EC-Council | Ethical hacking, understanding attacker techniques |

---

*References v1.0 | Last updated May 2026*
