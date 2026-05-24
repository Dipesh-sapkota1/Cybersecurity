# Incident Response Flow Diagram

This diagram illustrates the full decision-based response flow for a phishing incident at NexaCore Technologies, from initial detection through post-incident review.

Copy the Mermaid code below and paste it into [mermaid.live](https://mermaid.live) to render the diagram. You can also export it as a PNG or SVG from that site to include as an image in documentation or presentations.

---

## Response Flow — Mermaid Diagram

```mermaid
flowchart TD
    A([🔔 Phishing Report Received\nUser report / SIEM alert / M365 Defender]) --> B

    B[SOC Analyst: Open ServiceNow Ticket\nCollect email artifacts\nContact reporting user]

    B --> C{Was the email\ninteracted with?}

    C -->|No interaction| D[SEV-4 Low\nQuarantine email\nBlock sender domain]
    D --> E([✅ Ticket Closed\nNo further action])

    C -->|Opened only,\nno click| F[SEV-4 Low\nQuarantine email\nMonitor mailbox 48h]
    F --> E

    C -->|Link clicked| G{Were credentials\nentered?}

    G -->|No| H[SEV-3 Medium\nEscalate to IR Analyst\nSLA: 4 hours]
    H --> I[URL sandbox analysis\nURLScan.io / Any.run\nCheck Splunk for other\naffected users]
    I --> J{Other users\naffected?}
    J -->|Yes| K[Escalate severity\nNotify IR Lead]
    J -->|No| L[Quarantine + Block\nMonitor account 30 days]

    G -->|Yes — credentials entered| M[SEV-2 High\nCall IR Lead NOW\nSLA: 1 hour]
    M --> N[Azure AD sign-in\nlog investigation\nCheck for unauthorized\naccess or forwarding rules]
    N --> O{Evidence of\nlateral movement\nor data access?}
    O -->|Yes| P[🚨 Escalate to SEV-1 Critical\nPage CISO immediately\nNotify Legal]
    O -->|No| Q[Contain account\nDisable AzureAD account\nRevoke sessions\nReset password + MFA]

    C -->|Attachment opened\nor malware suspected| R[SEV-2 High\nCall IR Lead NOW]
    R --> S[CrowdStrike telemetry\nreview\nSandbox attachment\nin Any.run]
    S --> T{Malware execution\nconfirmed?}
    T -->|Yes| P
    T -->|No| Q

    P --> U[🔒 CONTAINMENT\nIsolate endpoint — CrowdStrike\nDisable account — Azure AD\nRevoke sessions + API keys\nBlock malicious IPs/domains at firewall]
    U --> V[🧹 ERADICATION\nRemove malware via CrowdStrike RTR\nDelete persistence mechanisms\nRemove unauthorized inbox rules\nAudit for backdoors]
    V --> W[♻️ RECOVERY\nReimage endpoint if required\nRe-enable account with new MFA\nVerify clean state\nRestore access gradually]
    W --> X[📋 POST-INCIDENT REVIEW\nWithin 5 business days\nTimeline reconstruction\nDetection gap measurement\nPlaybook update]

    Q --> X
    K --> Q
    L --> X
    X --> Y([✅ Incident Closed])

    style A fill:#4a90d9,color:#fff
    style P fill:#d9534f,color:#fff
    style U fill:#e8a838,color:#fff
    style V fill:#e8a838,color:#fff
    style W fill:#5cb85c,color:#fff
    style X fill:#5bc0de,color:#fff
    style Y fill:#5cb85c,color:#fff
    style E fill:#5cb85c,color:#fff
```

---

## How to View This Diagram

**Option 1 — Mermaid Live Editor (easiest)**
1. Go to [mermaid.live](https://mermaid.live)
2. Paste the code block above (without the triple backticks) into the editor
3. The diagram renders on the right side instantly
4. Click **Export → PNG** to download it for your project

**Option 2 — GitHub renders Mermaid automatically**
GitHub natively renders Mermaid diagrams inside Markdown files. If you paste the mermaid code block directly into any `.md` file in your repository, it will display as a rendered diagram on GitHub — no extra steps needed.

**Option 3 — VS Code**
Install the "Markdown Preview Mermaid Support" extension and open this file in preview mode.

---

## Diagram Legend

| Color | Meaning |
|---|---|
| 🔵 Blue | Trigger / Start point |
| 🔴 Red | Critical escalation |
| 🟠 Orange | Active containment / eradication |
| 🟢 Green | Recovery or resolution |
| 🔷 Teal | Review and closure |
