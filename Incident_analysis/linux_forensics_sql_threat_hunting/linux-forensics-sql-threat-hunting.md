# Linux Forensics & SQL Threat Hunting — NovaStar Logistics

**Classification:** Internal Security Investigation  
**Server:** `prod-web-01`  
**Incident Date:** January 15, 2024  
**Report Date:** January 15, 2024  
**Framework:** NIST SP 800-61 Rev. 2

---

## Executive Summary

On January 15, 2024, NovaStar Logistics' production web server `prod-web-01` suffered a confirmed security breach. An external attacker from IP `185.220.101.47` conducted a brute-force SSH attack beginning at 02:50 AM, successfully authenticating as the `deploy` service account at 02:54 AM after 112 failed attempts. Following initial access, the attacker performed SQL injection reconnaissance against the web application, established persistence by creating a backdoor account (`sysbackup`), and exfiltrated approximately **83.6 MB** of sensitive data including a full user database dump and backup archive.

> **Impact:** Confirmed data breach — user credentials and backup archives exfiltrated. Backdoor persistence established. Two attack IPs identified.

---

## Part 1 — Linux Log Investigation

### Task 1.1 — Brute Force Identification

**Command Used:**
```bash
grep 'Failed password' auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | head -20
```

**Findings:**

| IP Address | Failed Attempts | Pattern |
|---|---|---|
| `185.220.101.47` | 112 | Every ~2 seconds, 02:50–02:54 AM; targeted root, admin, deploy, webmaster, ubuntu |
| `91.108.4.200` | 28 | Slower pace, starting 03:02 AM; exclusively targeted `root` |

**2 unique IPs** attempted failed logins. `185.220.101.47` was the most aggressive with 112 attempts — a classic automated brute-force signature consistent with tools like Hydra or Medusa.

---

### Task 1.2 — Successful Login Analysis

**Command Used:**
```bash
grep 'Accepted password' auth.log | awk '{print $11, $9}'
```

**Findings:**

The attack was **successful**. IP `185.220.101.47` authenticated as user `deploy` at **02:54:12 AM** via password authentication.

Three indicators confirm this is malicious:

1. The source IP is external (non-RFC1918) — all legitimate logins originated from `10.0.1.x` internal addresses
2. All legitimate users (carol, sysadmin, dave) authenticated via **public key** — not password
3. The successful login followed 112 failed attempts from the exact same IP in a 4-minute window

---

### Task 1.3 — Persistence: Backdoor Account Creation

**Commands Used:**
```bash
grep 'new user' auth.log
grep 'useradd' auth.log
```

**Findings:**

A backdoor account was created at **03:18:44 AM** — 24 minutes after initial breach:

| Field | Value |
|---|---|
| Username | `sysbackup` |
| UID / GID | 1002 |
| Home Directory | `/home/sysbackup` |
| Shell | `/bin/bash` (full interactive shell) |

The name `sysbackup` is deliberately chosen to blend in as a legitimate system/maintenance account. A password was set immediately after creation (`passwd[3302]`), making it a fully functional re-entry point independent of the `deploy` account.

---

### Task 1.4 — Complete Attack Timeline

| Timestamp | Event | MITRE ATT&CK |
|---|---|---|
| Jan 15 01:06–01:59 | Legitimate users (carol, sysadmin, dave) log in via SSH public key from `10.0.1.x` | — |
| Jan 15 02:50:00 | **Brute-force begins:** `185.220.101.47` starts rapid password guessing (~2s intervals) targeting root, admin, deploy, webmaster, ubuntu | T1110.001 — Brute Force: Password Guessing |
| Jan 15 02:54:12 | **BREACH:** Attacker authenticates as `deploy` via password after 112 failed attempts | T1078 — Valid Accounts |
| Jan 15 02:54:12 | Session opened for `deploy` by UID=0 (root process confirms active shell) | T1059.004 — Unix Shell |
| Jan 15 02:55:01 | Attacker begins SQL injection probing on web app via sqlmap | T1190 — Exploit Public-Facing Application |
| Jan 15 03:02:00 | Second IP (`91.108.4.200`) begins brute-forcing `root` — does not succeed | T1110.001 |
| Jan 15 03:05:11 | `91.108.4.200` attempts SQL injection on `/admin/` endpoint (blocked, 403) | T1190 |
| Jan 15 03:14:22 | Attacker (`deploy` session) performs `file_download` action in web app | T1005 — Data from Local System |
| Jan 15 03:18:44 | **Persistence:** Attacker creates backdoor account `sysbackup` (UID=1002), sets password | T1136.001 — Create Account: Local Account |
| Jan 15 03:47:15 | Attacker performs `data_export` — mass data exfiltration begins | T1048 — Exfiltration Over Alternative Protocol |
| Jan 15 03:47–03:58 | **Exfiltration:** `backup_users_ALL.tar.gz` (52.4 MB) + `db_dump_full.sql.gz` (31.2 MB) sent to `185.220.101.47` — **83.6 MB total** | T1020 — Automated Exfiltration |

---

## Part 2 — SQL Threat Hunting

### Task 2.1 — Active Sessions During Attack Window (03:00–04:00 AM)

**Query Used:**
```sql
SELECT username, ip_address, login_time, action
FROM user_sessions
WHERE login_time BETWEEN '2024-01-15 03:00:00' AND '2024-01-15 04:00:00'
ORDER BY login_time;
```

**Results:**

| username | ip_address | login_time | action |
|---|---|---|---|
| deploy | 185.220.101.47 | 2024-01-15 03:14:22 | file_download |
| deploy | 185.220.101.47 | 2024-01-15 03:47:15 | data_export |

**Analysis:** Only the `deploy` account was active between 03:00–04:00 AM, exclusively from the attacker IP `185.220.101.47`. No legitimate employee accounts were active at this hour. Both session tokens (`tok_ATTACKER`, `tok_ATTACKER2`) confirm a single attacker operating two sequential sessions.

---

### Task 2.2 — Abnormal Data Exports (Exfiltration Evidence)

**Query Used:**
```sql
SELECT username, COUNT(*) AS export_count, SUM(bytes_transferred) AS total_bytes
FROM data_exports
WHERE export_date = '2024-01-15'
GROUP BY username
HAVING total_bytes > 10000000
ORDER BY total_bytes DESC;
```

**Results:**

| username | export_count | total_bytes |
|---|---|---|
| deploy | 2 | 83,630,000 bytes (~83.6 MB) |

**Exfiltrated Files:**

| File | Size | Destination |
|---|---|---|
| `backup_users_ALL.tar.gz` | 52,430,000 bytes (52.4 MB) | `185.220.101.47` |
| `db_dump_full.sql.gz` | 31,200,000 bytes (31.2 MB) | `185.220.101.47` |

**Context:** The largest legitimate export (carol's `customer_list_q4.csv`) was 980,200 bytes (~0.98 MB). The attacker exported **85× more data** than the largest normal export — a definitive exfiltration signature.

---

### Task 2.3 — SQL Injection Detection

**Query Used:**
```sql
SELECT ip_address, request_url, timestamp
FROM access_logs
WHERE request_url LIKE '%UNION%'
   OR request_url LIKE '%SELECT%'
   OR request_url LIKE '%DROP%'
   OR request_url LIKE "%'%"
ORDER BY timestamp;
```

**Results — 5 SQL Injection Attempts from 2 IPs:**

| ip_address | request_url | timestamp | Technique |
|---|---|---|---|
| `185.220.101.47` | `/login.php?user=' OR '1'='1&pass=x` | 02:55:22 | Auth bypass — always-true condition |
| `185.220.101.47` | `/search.php?q=' UNION SELECT username,password,3 FROM users--` | 02:55:45 | Data extraction — credential dump |
| `185.220.101.47` | `/products.php?id=1' AND SLEEP(5)--` | 02:56:01 | Time-based blind SQLi — injection probe |
| `185.220.101.47` | `/login.php?user=admin' DROP TABLE users--&pass=x` | 02:56:14 | Destructive — attempted table deletion |
| `91.108.4.200` | `/admin/' OR 1=1--` | 03:05:11 | Admin panel auth bypass (returned 403 — blocked) |

**Analysis:** `185.220.101.47` deployed a multi-stage SQL injection campaign consistent with automated tooling (sqlmap/1.7 UA confirmed). Payloads escalate from reconnaissance (auth bypass, data extraction) to destructive intent (DROP TABLE). The second IP attempted admin panel access but was blocked by the server's existing 403 controls.

---

## Part 3 — Incident Report

### Root Cause

Two compounding failures enabled this breach:

1. **Password authentication was enabled on SSH for the `deploy` account.** All legitimate users authenticated via public key — `deploy` should have been restricted identically. This single misconfiguration was the attack's entry point.

2. **No rate-limiting, account lockout, or IP-based blocking was in place.** 112 login attempts from one external IP over 4 minutes went completely undetected and unblocked. An industry-standard fail2ban configuration with a 5-attempt threshold would have terminated this attack within its first 10 seconds.

---

### Evidence Summary

| # | Source | Timestamp | Entry |
|---|---|---|---|
| 1 | `auth.log` | Jan 15 02:50:00 | `Failed password for root from 185.220.101.47 port 62833 ssh2` — first of 112 brute-force attempts |
| 2 | `auth.log` | Jan 15 02:54:12 | `Accepted password for deploy from 185.220.101.47 port 52341 ssh2` — confirmed breach |
| 3 | `auth.log` | Jan 15 03:18:44 | `useradd[3301]: new user: name=sysbackup, UID=1002` — persistence established |
| 4 | `access_logs` | Jan 15 02:55:45 | `GET /search.php?q=' UNION SELECT username,password,3 FROM users--` (sqlmap/1.7) — credential dump attempt |
| 5 | `data_exports` | Jan 15 03:47–03:58 | `deploy` exported 83.6 MB across 2 files to `185.220.101.47` |
| 6 | `user_sessions` | Jan 15 03:14:22 & 03:47:15 | Two attacker sessions: `file_download` then `data_export`, both from `185.220.101.47` |

---

### Immediate Containment (Next 30 Minutes)

> Priority: stop active attacker access before any remediation work begins.

```bash
# 1. Block attacker IPs at firewall
iptables -I INPUT -s 185.220.101.47 -j DROP
iptables -I INPUT -s 91.108.4.200 -j DROP

# 2. Terminate active sessions
who                          # confirm active sessions
pkill -u deploy
pkill -u sysbackup

# 3. Lock compromised accounts
usermod -L deploy
usermod -L sysbackup

# 4. Remove backdoor account
userdel -r sysbackup

# 5. Preserve evidence BEFORE further changes
dd if=/dev/sda of=/forensics/prod-web-01.img bs=4M
cp -a /var/log /forensics/logs-snapshot/
```

**Stakeholder notifications required:** Security team, management, and legal — confirmed PII/credential exfiltration (83.6 MB of user data triggers GDPR Article 33 notification obligations within 72 hours).

---

### Long-Term Remediation

**Control 1 — Disable SSH password authentication globally**

```bash
# /etc/ssh/sshd_config
PasswordAuthentication no
ChallengeResponseAuthentication no
```

This single change blocks the entire attack vector. Public key authentication must be enforced for all accounts without exception, including service accounts.

**Control 2 — Deploy fail2ban with aggressive SSH thresholds**

```ini
# /etc/fail2ban/jail.local
[sshd]
enabled  = true
maxretry = 5
findtime = 60
bantime  = 3600
```

112 attempts over 4 minutes would trigger an automatic ban within the first 10 seconds at these settings.

**Control 3 — Web Application Firewall (WAF) with SQLi signatures**

The sqlmap payloads used (`UNION SELECT`, `SLEEP()`, `DROP TABLE`, `OR 1=1`) are in every major WAF signature set (ModSecurity CRS, AWS WAF, Cloudflare). Blocking at the edge prevents reconnaissance before it reaches the application layer.

**Bonus — Principle of Least Privilege for service accounts**

The `deploy` account should have no interactive shell, no password set, and permissions scoped strictly to deployment operations. A service account that can initiate `data_export` actions is over-privileged by design.

---

## Bonus — One-Line Forensic Bash Command

Extract all unique IPs from `auth.log`, perform reverse DNS lookup on each, and save to `suspicious_ips.txt`:

```bash
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' auth.log \
  | sort -u \
  | while read ip; do
      echo "$ip: $(host $ip | head -1)"
    done > suspicious_ips.txt
```

**Breakdown:**

| Component | Purpose |
|---|---|
| `grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}'` | Regex-extracts every IPv4 address from the log |
| `sort -u` | Deduplicates — each IP processed once |
| `while read ip; do ... done` | Iterates over each unique IP |
| `host $ip \| head -1` | Reverse DNS lookup (e.g., `185.220.101.47` → tor-exit-node) |
| `> suspicious_ips.txt` | Saves all results to file |

---

## References

| Resource | Relevance |
|---|---|
| [MITRE ATT&CK T1110.001 — Brute Force](https://attack.mitre.org/techniques/T1110/001/) | SSH brute-force pattern |
| [MITRE ATT&CK T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/) | `deploy` account compromise |
| [MITRE ATT&CK T1136.001 — Create Local Account](https://attack.mitre.org/techniques/T1136/001/) | `sysbackup` backdoor |
| [MITRE ATT&CK T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | SQL injection via web app |
| [MITRE ATT&CK T1048 — Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/) | 83.6 MB data exfiltration |
| [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) | Incident handling lifecycle |
| [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) | SQLi payload classification |
| [fail2ban Documentation](https://www.fail2ban.org/wiki/index.php/MANUAL_0_8) | SSH rate-limiting implementation |
