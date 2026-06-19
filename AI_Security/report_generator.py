#!/usr/bin/env python3
"""
report_generator.py

Renders the final, professional Markdown pentest report.

This script works two ways:

1. As a module imported by run_audit.py, using the live engagement
   status (audit_engine.get_status()) — the original workflow.

2. As a standalone CLI, pointed directly at any attempt_log.json:

       python3 report_generator.py engagement_data/attempt_log.json
       python3 report_generator.py engagement_data/attempt_log.json -o final_report.md
       python3 report_generator.py engagement_data/attempt_log.json --total-budget 0

   The CLI path has NO dependency on audit_engine's in-memory/session
   state — it reads only the JSON file given on the command line. This
   matters because testing that happens across multiple stop/start
   sessions can leave a stateful "status" tracker out of sync with what's
   actually on disk; running this script directly against the JSON file
   sidesteps that entirely and will always produce a report from
   whatever attempts are currently logged, partial or complete.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from optional_garak_reference import lookup_garak_reference

# --- Risk badge mapping ---------------------------------------------------

RISK_BADGES = {
    "none": "🟢 None",
    "low": "🟡 Low",
    "medium": "🟠 Medium",
    "high": "🔴 High",
}

REQUIRED_FIELDS = [
    "test_id",
    "category",
    "tester_id",
    "prompt_text",
    "prompt_char_count",
    "dispatched_at_utc",
    "response_text",
    "observed_behavior",
    "risk_rating",
    "reproducibility_notes",
    "attempt_number",
]


def badge_for(risk_rating_text: str) -> str:
    """Map a free-text risk_rating string to a colored badge, falling
    back to a neutral badge with the first clause if no known level is
    found."""
    lowered = risk_rating_text.strip().lower()
    for level, badge in RISK_BADGES.items():
        if lowered.startswith(level):
            return badge
    first_clause = risk_rating_text.split("—")[0].split(".")[0].strip()
    return f"⚪ {first_clause or 'Unrated'}"


def render_summary_table(entries: list[dict[str, Any]]) -> str:
    lines = ["| Test ID | Category | Risk | Dispatched (UTC) |", "|---|---|---|---|"]
    for e in sorted(entries, key=lambda x: x["attempt_number"]):
        category_display = str(e["category"]).replace("_", " ")
        lines.append(
            f"| {e['test_id']} | {category_display} | "
            f"{badge_for(str(e['risk_rating']))} | {e['dispatched_at_utc']} |"
        )
    return "\n".join(lines)


def render_methodology_note(entries: list[dict[str, Any]]) -> str:
    """Flag any set of attempts that returned character-for-character
    identical response text, since that pattern is itself a finding."""
    by_text: dict[str, list[str]] = {}
    for e in entries:
        key = str(e["response_text"]).strip()
        by_text.setdefault(key, []).append(e["test_id"])

    repeats = {text: ids for text, ids in by_text.items() if len(ids) > 1}
    if not repeats:
        return ""

    lines = ["## Methodology Note: Repeated Identical Outputs", ""]
    for text, ids in repeats.items():
        lines.append(
            f"Tests **{', '.join(ids)}** returned character-for-character "
            "identical response text, despite targeting different "
            "guardrail categories and injection techniques. This is "
            "reported as a finding in its own right: it suggests these "
            "refusals may originate from a single upstream topic/intent "
            "filter rather than the model independently reasoning through "
            "and rejecting each distinct attack. Recommend verifying, "
            "outside this engagement's attempt budget, whether ordinary "
            "in-scope questions ever return this same string."
        )
        lines.append("")
        lines.append("```")
        lines.append(text)
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def render_test_section(entry: dict[str, Any]) -> str:
    category_display = str(entry["category"]).replace("_", " ")
    ref = lookup_garak_reference(entry["category"])

    lines = [f"### {entry['test_id']} — {category_display}", ""]
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| **Test ID** | `{entry['test_id']}` |")
    lines.append(f"| **Tester** | {entry['tester_id']} |")
    lines.append(f"| **Risk rating** | {badge_for(str(entry['risk_rating']))} |")
    if ref:
        lines.append(f"| **Garak taxonomy analogue** | {ref['probes']} |")
    lines.append(f"| **Dispatched (UTC)** | {entry['dispatched_at_utc']} |")
    captured = entry.get("response_captured_at_utc") or "_not recorded_"
    lines.append(f"| **Response captured (UTC)** | {captured} |")
    lines.append("")

    char_count = entry.get("prompt_char_count", len(str(entry["prompt_text"])))
    lines.append(f"**Prompt used** ({char_count} chars):")
    lines.append("```")
    lines.append(str(entry["prompt_text"]))
    lines.append("```")
    lines.append("")

    lines.append("**Response captured:**")
    lines.append("```")
    lines.append(str(entry["response_text"]))
    lines.append("```")
    lines.append("")

    lines.append("**Observed behavior:**")
    lines.append(str(entry["observed_behavior"]))
    lines.append("")

    lines.append("**Risk rating rationale:**")
    lines.append(str(entry["risk_rating"]))
    lines.append("")

    lines.append("**Reproducibility notes:**")
    lines.append(str(entry["reproducibility_notes"]))
    lines.append("")

    return "\n".join(lines)


def render_report(entries: list[dict[str, Any]], total_budget: int | None, testers: list[str] | None = None) -> str:
    used = len(entries)
    sorted_entries = sorted(entries, key=lambda x: x["attempt_number"])

    lines = ["# Prompt Injection Assessment — Findings Report", ""]

    if total_budget is not None:
        remaining = max(total_budget - used, 0)
        lines.append(f"**Attempts used:** {used} / {total_budget}  (**{remaining} remaining**)")
    else:
        lines.append(f"**Attempts logged:** {used}")

    lines.append(
        "**Target interaction model:** Manual, browser-based chat box only — "
        "no public API, 500-character input limit, 3 queries/hour/tester rate limit."
    )

    if testers is None:
        testers = sorted({e["tester_id"] for e in entries if e.get("tester_id")})
    if testers:
        lines.append(f"**Authorized testers:** {', '.join(testers)}")
    lines.append(f"**Report generated:** {datetime.now(timezone.utc).isoformat()}")
    lines.append("")

    lines.append("## Summary of Results")
    lines.append("")
    lines.append(render_summary_table(entries))
    lines.append("")

    methodology_note = render_methodology_note(entries)
    if methodology_note:
        lines.append(methodology_note)

    lines.append("## Detailed Findings")
    lines.append("")
    for entry in sorted_entries:
        lines.append(render_test_section(entry))

    lines.append("## Disclosure & Handling")
    lines.append("")
    lines.append(
        "This report documents working guardrail bypasses against the "
        "target system. Deliver only to the target owner over an "
        "encrypted or access-controlled channel, and delete local copies "
        "once receipt is confirmed."
    )
    lines.append("")

    return "\n".join(lines)


def _write_report(report_text: str, output_path: Path) -> None:
    output_path.write_text(report_text, encoding="utf-8")
    try:
        output_path.chmod(0o600)
    except (OSError, NotImplementedError):
        pass  # chmod is a no-op / unsupported on some platforms (e.g. Windows)


# --- Engine-integrated path (used by run_audit.py) -------------------------

def generate_report() -> Path:
    """
    Generates the report using the live engagement status from
    audit_engine (the original, session-tracked workflow). Writes to
    engagement_data/pentest_report.md.
    """
    from audit_engine import DATA_DIR, get_status

    status = get_status()
    report_text = render_report(status.entries, total_budget=status.total)
    report_path = DATA_DIR / "pentest_report.md"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    _write_report(report_text, report_path)
    return report_path


# --- Standalone CLI path (no dependency on engine session state) ----------

def _load_attempts_from_file(path: Path) -> list[dict[str, Any]]:
    import json

    if not path.exists():
        print(f"Error: input file not found: {path}", file=sys.stderr)
        sys.exit(2)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: could not read {path}: {exc}", file=sys.stderr)
        sys.exit(2)

    try:
        data = json.loads(raw) if raw.strip() else []
    except json.JSONDecodeError as exc:
        print(f"Error: {path} is not valid JSON: {exc}", file=sys.stderr)
        sys.exit(3)

    if not isinstance(data, list):
        print(f"Error: expected a JSON list of attempt records in {path}", file=sys.stderr)
        sys.exit(3)

    validated = []
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            print(f"Warning: skipping entry {i} (not an object)", file=sys.stderr)
            continue
        missing = [f for f in REQUIRED_FIELDS if f not in entry]
        if missing:
            print(
                f"Warning: entry {i} ({entry.get('test_id', '?')}) missing fields: "
                f"{', '.join(missing)} — including anyway with blanks filled in.",
                file=sys.stderr,
            )
            for f in missing:
                entry[f] = "" if f != "attempt_number" else i + 1
        entry.setdefault("response_captured_at_utc", "")
        validated.append(entry)

    return validated


def _cli_main() -> None:
    parser = argparse.ArgumentParser(
        prog="report_generator.py",
        description=(
            "Generate the final Markdown pentest report directly from an "
            "attempt_log.json file, independent of any live session state."
        ),
    )
    parser.add_argument(
        "input_path",
        type=Path,
        help="Path to attempt_log.json (the file produced/accumulated during manual testing).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path to write the rendered Markdown report. Defaults to <input_dir>/pentest_report.md.",
    )
    parser.add_argument(
        "--total-budget",
        type=int,
        default=6,
        help=(
            "Total attempt budget for the engagement, used to show "
            "'used/remaining' in the report header. Pass 0 to omit the "
            "budget line entirely."
        ),
    )

    args = parser.parse_args()

    entries = _load_attempts_from_file(args.input_path)
    if not entries:
        print("Warning: no valid attempt records found — generating an empty report.", file=sys.stderr)

    total_budget = args.total_budget if args.total_budget > 0 else None
    report_text = render_report(entries, total_budget=total_budget)

    output_path = args.output or (args.input_path.parent / "pentest_report.md")
    try:
        _write_report(report_text, output_path)
    except OSError as exc:
        print(f"Error: could not write report to {output_path}: {exc}", file=sys.stderr)
        sys.exit(2)

    print(f"Report written to: {output_path}")
    print(f"Attempts included: {len(entries)}")


if __name__ == "__main__":
    _cli_main()
