# Controls & Compliance Assessment Checklist — Botium Toys

**Document Type:** Controls & Compliance Checklist
**Classification:** Confidential
**Framework References:** NIST SP 800-53, PCI DSS v3.2.1, GDPR, SOC 2
**Version:** 1.0
**Prepared By:** Security Consulting Team

---

## Part 1 — Controls Assessment Checklist

*Does Botium Toys currently have this control in place?*

| Status | Control | Control Type | Finding |
|--------|---------|-------------|---------|
| ❌ No | **Least Privilege** | Technical / Administrative | All employees have unrestricted access to customer data including PII and cardholder data |
| ❌ No | **Disaster Recovery Plans** | Administrative | No backup of critical data; no DRP documented or tested |
| ⚠️ Partial | **Password Policies** | Administrative | Policy exists but requirements are nominal and below minimum complexity standards |
| ❌ No | **Separation of Duties** | Administrative | No hierarchical role structure defined; single employees can perform high-risk actions |
| ✅ Yes | **Firewall** | Technical | Rule-based firewall maintained by IT team; traffic monitoring active |
| ❌ No | **Intrusion Detection System (IDS)** | Technical | No IDS deployed; lateral movement and anomalous traffic would go undetected |
| ❌ No | **Backups** | Technical / Operational | No critical data backups; complete data loss possible after a destructive event |
| ✅ Yes | **Antivirus Software** | Technical | Installed and regularly monitored by IT Department |
| ⚠️ Partial | **Legacy System Monitoring** | Operational | Maintenance performed but no defined schedule; intervention procedures unclear |
| ❌ No | **Encryption** | Technical | No encryption at rest or in transit; customer card data stored in plaintext |
| ❌ No | **Password Management System** | Technical | No compliant centralized system; manual resets create IT backlogs |
| ✅ Yes | **Locks (offices, storefront, warehouse)** | Physical | All facilities have adequate physical locks |
| ✅ Yes | **CCTV Surveillance** | Physical | Fully functional CCTV; monitored by IT Department |
| ✅ Yes | **Fire Detection / Prevention** | Physical | Fire alarm and sprinkler systems functioning |

### Controls Summary

| Control Type | Implemented | Partial | Not Implemented |
|-------------|------------|---------|----------------|
| Technical | 2 | 2 | 4 |
| Administrative | 0 | 1 | 3 |
| Physical | 3 | 0 | 0 |
| **Total** | **5** | **3** | **7** |

---

## Part 2 — Compliance Checklist

### 2.1 Payment Card Industry Data Security Standard (PCI DSS)

*Does Botium Toys currently adhere to this PCI DSS best practice?*

| Status | Requirement | Finding |
|--------|------------|---------|
| ❌ No | Only authorized users have access to customers' credit card information | All employees have access to PII; no role-based access controls implemented |
| ❌ No | Credit card information is accepted, processed, transmitted, and stored in a secure environment | Credit card data processed internally in an unencrypted environment |
| ❌ No | Implement data encryption for credit card transaction touchpoints and stored data | All cardholder data managed without encryption in local database |
| ❌ No | Adopt secure password management policies | Password management policy does not meet current minimum complexity requirements |

**PCI DSS Compliance Status: 0 / 4 requirements met — NON-COMPLIANT**

---

### 2.2 General Data Protection Regulation (GDPR)

*Does Botium Toys currently adhere to this GDPR best practice?*

| Status | Requirement | Finding |
|--------|------------|---------|
| ❌ No | EU customers' data is kept private and secured | No supporting evidence for the safety of customer data given absent encryption and IAM controls |
| ✅ Yes | Plan in place to notify EU customers within 72 hours of a breach | Notification plan established and enforced by IT team |
| ❌ No | Data is properly classified and inventoried | Asset classification missing; first function of cybersecurity lifecycle (Identify) not completed |
| ✅ Yes | Privacy policies, procedures, and processes enforced | Privacy policies documented and enforced among IT and other departments |

**GDPR Compliance Status: 2 / 4 requirements met — PARTIAL**

---

### 2.3 System and Organizations Controls (SOC 2)

*Does Botium Toys currently adhere to these SOC 2 trust principles?*

| Status | Requirement | Finding |
|--------|------------|---------|
| ❌ No | User access policies are established | Distinct roles and duties segmentation not implemented |
| ❌ No | Sensitive data (PII/SPII) is confidential and private | Encryption not implemented; data accessible to all employees |
| ✅ Yes | Data integrity ensures data is consistent, complete, accurate, and validated | IT Department maintains availability and integrity controls |
| ✅ Yes | Data is available to individuals authorized to access it | IT Department has ensured data availability and integrated integrity controls |

**SOC 2 Compliance Status: 2 / 4 requirements met — PARTIAL**

---

## Part 3 — Overall Compliance Posture

| Framework | Requirements Met | Total | Compliance % | Status |
|-----------|----------------|-------|-------------|--------|
| PCI DSS | 0 | 4 | 0% | 🔴 Non-Compliant |
| GDPR | 2 | 4 | 50% | 🟠 Partial |
| SOC 2 | 2 | 4 | 50% | 🟠 Partial |

---

## Part 4 — Recommendations

To improve security posture and achieve compliance, Botium Toys must prioritize the following:

**Administrative Controls:**
- Implement Least Privilege and role-based access
- Enforce Separation of Duties across critical functions
- Document and test Disaster Recovery Plans
- Strengthen and enforce Password Policy

**Technical Controls:**
- Deploy an Intrusion Detection System (IDS)
- Implement data encryption at rest and in transit
- Establish compliant Password Management System
- Perform critical data backups on a defined schedule
- Define legacy system intervention procedures

**Compliance Actions:**
- Properly classify and inventory all assets (GDPR / NIST Identify)
- Restrict access to cardholder data (PCI DSS Req. 7)
- Establish user access policies with unique user IDs (SOC 2 / PCI DSS Req. 8)
