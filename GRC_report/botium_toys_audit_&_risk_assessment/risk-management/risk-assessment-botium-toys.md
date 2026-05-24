# Risk Assessment Report — Botium Toys

**Document Type:** Internal Security Risk Assessment
**Classification:** Confidential
**Version:** 1.0
**Prepared By:** Security Consulting Team
**Review Date:** [Insert Date]

---

## 1. Scope and Goals

### Scope
The scope of this assessment encompasses the **entire security program at Botium Toys**. All assets managed by the IT Department are included, alongside internal processes and procedures related to controls implementation and compliance best practices.

### Goals
- Assess all existing assets against security control requirements
- Complete the controls and compliance checklist
- Identify which controls and compliance best practices require implementation
- Improve Botium Toys' overall security posture

---

## 2. Asset Inventory

The following assets are under management by the IT Department:

| Asset Category | Examples |
|---------------|---------|
| **On-Premises Equipment** | Office hardware, networking gear |
| **Employee Devices** | Desktops, laptops, smartphones, remote workstations, peripherals |
| **Physical Security Assets** | Surveillance cameras, cable infrastructure |
| **Retail Assets** | Storefront products, warehouse inventory |
| **Systems & Software** | Accounting, telecommunications, database, security, e-commerce, inventory management |
| **Network Infrastructure** | Internet access, internal LAN |
| **Data Assets** | Data retention systems, storage infrastructure |
| **Legacy Systems** | End-of-life systems requiring human monitoring |

---

## 3. Risk Description

Botium Toys currently exhibits **inadequate asset management** and lacks the necessary security controls to meet U.S. and international regulatory requirements. This creates significant exposure to both operational disruption and regulatory penalties.

---

## 4. Risk Score

| Metric | Rating |
|--------|--------|
| **Overall Risk Score** | **8 / 10** |
| **Asset Loss Potential Impact** | Medium |
| **Regulatory/Compliance Risk** | High |
| **Control Implementation Status** | Insufficient |

> **Justification:** The risk score of 8/10 reflects the combination of absent critical controls (encryption, IDS, DRP) and incomplete compliance adherence across PCI DSS and GDPR obligations.

---

## 5. Detailed Findings

### 5.1 Access Control

| Finding | Status |
|---------|--------|
| All employees have unrestricted access to internally stored data | ⚠️ Identified |
| Access to cardholder data and PII/SPII is not restricted | ⚠️ Identified |
| Least privilege principle not implemented | ❌ Not in place |
| Separation of duties not enforced | ❌ Not in place |

### 5.2 Data Protection

| Finding | Status |
|---------|--------|
| Encryption not applied to customer credit card data | ❌ Not in place |
| Data at rest unencrypted in internal database | ❌ Not in place |
| Data in transit not encrypted | ❌ Not in place |

### 5.3 Network Security

| Finding | Status |
|---------|--------|
| Firewall with defined rule set in place | ✅ Implemented |
| Intrusion Detection System (IDS) absent | ❌ Not in place |

### 5.4 Endpoint Security

| Finding | Status |
|---------|--------|
| Antivirus software installed and monitored | ✅ Implemented |

### 5.5 Identity & Credential Management

| Finding | Status |
|---------|--------|
| Password policy exists but non-compliant with complexity requirements | ⚠️ Partial |
| No centralized password management system | ❌ Not in place |
| Manual password resets causing IT backlog | ⚠️ Operational Impact |

### 5.6 Availability & Business Continuity

| Finding | Status |
|---------|--------|
| No disaster recovery plans documented | ❌ Not in place |
| No backups of critical data | ❌ Not in place |
| Data integrity maintained by IT Department | ✅ Implemented |

### 5.7 Legacy Systems

| Finding | Status |
|---------|--------|
| Legacy systems monitored and maintained | ✅ Implemented |
| No regular maintenance schedule defined | ⚠️ Partial |
| Intervention methods unclear | ⚠️ Partial |

### 5.8 Regulatory Compliance

| Finding | Status |
|---------|--------|
| EU customer 72-hour breach notification plan in place | ✅ Implemented |
| Privacy policies, procedures documented and enforced | ✅ Implemented |

### 5.9 Physical Security

| Finding | Status |
|---------|--------|
| Adequate locks at main offices, storefront, and warehouse | ✅ Implemented |
| CCTV surveillance operational and up to date | ✅ Implemented |
| Fire detection and prevention systems functioning | ✅ Implemented |

---

## 6. Control Best Practices — NIST CSF Alignment

The **Identify** function of the NIST CSF requires organizations to maintain a complete, classified asset inventory as the foundation for risk management. Botium Toys must:

1. Allocate dedicated resources to conduct formal asset identification
2. Classify existing assets by sensitivity and business criticality
3. Determine the potential business impact from loss of each asset class

---

## 7. Risk Summary Matrix

| Risk Area | Likelihood | Impact | Risk Level |
|-----------|-----------|--------|-----------|
| PII/Cardholder data exposure | High | High | 🔴 Critical |
| Ransomware / Malware attack | High | High | 🔴 Critical |
| Data breach via unencrypted DB | High | High | 🔴 Critical |
| Business disruption (no DRP) | Medium | High | 🔴 Critical |
| Regulatory fine (GDPR/PCI DSS) | High | High | 🔴 Critical |
| Unauthorized access (no IAM) | High | Medium | 🟠 High |
| Legacy system compromise | Medium | Medium | 🟠 High |
| Weak credential exploitation | High | Medium | 🟠 High |

---

## 8. Recommendations Summary

To reduce risk to an acceptable level, Botium Toys must prioritize implementation of the following controls:

1. **Data Encryption** — Implement encryption at rest (SC-28) and in transit (SC-8) for all PII and cardholder data
2. **Intrusion Detection System** — Deploy IDS/IPS on the internal network (SI-4)
3. **Disaster Recovery Plan** — Document and test DRP and backup procedures (CP-2, CP-9)
4. **Access Control / Least Privilege** — Enforce role-based access and separation of duties (AC-3, AC-6)
5. **Password Policy Enforcement** — Deploy compliant centralized password management (IA-5)
6. **Multi-Factor Authentication** — Implement MFA for all critical system access (IA-2)

---

*Document prepared based on the Botium Toys internal security program assessment.*
*All findings are based on the asset inventory and IT controls review as documented in the audit scope.*
