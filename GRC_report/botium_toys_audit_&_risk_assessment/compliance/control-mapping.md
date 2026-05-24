# Control Mapping — Cross-Framework Reference

**Document Type:** Control Mapping
**Version:** 1.0

---

## NIST SP 800-53 → PCI DSS → GDPR → SOC 2

| Control Area | NIST SP 800-53 | PCI DSS Req. | GDPR Article | SOC 2 Criterion | Status |
|-------------|---------------|-------------|-------------|----------------|--------|
| Firewall / Network Controls | SC-7 | Req. 1 | Art. 32 | CC6.6 | ✅ |
| Malware Protection | SI-3 | Req. 5 | Art. 32 | CC7.1 | ✅ |
| Physical Access Controls | PE-3 | Req. 9 | Art. 32 | CC6.4 | ✅ |
| Breach Notification | IR-6 | Req. 12.10 | Art. 33, 34 | CC2.2 | ✅ |
| Privacy Policies | AR-1 | Req. 12 | Art. 24, 25 | P1.1 | ⚠️ |
| Data Encryption at Rest | SC-28 | Req. 3 | Art. 32 | C1.2 | ❌ |
| Data Encryption in Transit | SC-8 | Req. 4 | Art. 32 | C1.2 | ❌ |
| Access Control / Least Privilege | AC-3, AC-6 | Req. 7 | Art. 5, 25 | CC6.3 | ❌ |
| Separation of Duties | AC-5 | Req. 6.4 | Art. 32 | CC6.3 | ❌ |
| Multi-Factor Authentication | IA-2 | Req. 8.3 | Art. 32 | CC6.1 | ❌ |
| Password Management | IA-5 | Req. 8.2, 8.6 | Art. 32 | CC6.2 | ❌ |
| Intrusion Detection | SI-4 | Req. 11.4 | Art. 32 | CC7.2 | ❌ |
| Audit Logging / SIEM | AU-2, AU-12 | Req. 10 | Art. 32 | CC7.2 | ❌ |
| Backup / Recovery | CP-9 | Req. 12 | Art. 32 | A1.2 | ❌ |
| Contingency Plan / DRP | CP-2 | Req. 12 | Art. 32 | A1.2 | ❌ |
| Incident Response Plan | IR-4, IR-8 | Req. 12.10 | Art. 33 | CC7.4 | ❌ |
| Asset Classification | CM-8, RA-2 | Req. 2, 9 | Art. 5 | C1.1 | ❌ |

**Legend:** ✅ Implemented | ⚠️ Partial | ❌ Not Implemented
