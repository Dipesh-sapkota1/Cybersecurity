"""
audit_engine.py

Budget tracking, attempt dispatch/capture, JSON + CSV persistence, and
file-permission hardening for the manual prompt-injection engagement.

No network calls happen anywhere in this module — all data stays local.
"""

from __future__ import annotations

import csv
import json
import os
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from audit_config import ENGAGEMENT_BUDGET, TEST_SUITE

DATA_DIR = Path(__file__).resolve().parent / "engagement_data"
LOG_JSON = DATA_DIR / "attempt_log.json"
LOG_CSV = DATA_DIR / "attempt_log.csv"

CSV_COLUMNS = [
    "test_id",
    "category",
    "tester_id",
    "prompt_text",
    "prompt_char_count",
    "dispatched_at_utc",
    "response_text",
    "response_captured_at_utc",
    "observed_behavior",
    "risk_rating",
    "reproducibility_notes",
    "attempt_number",
]


def _harden_permissions(target: Path, is_dir: bool = False) -> None:
    """Lock a file/directory to owner-only permissions on POSIX systems."""
    if os.name != "posix":
        return  # chmod is a no-op on Windows
    try:
        target.chmod(0o700 if is_dir else 0o600)
    except OSError as exc:
        print(f"Warning: could not set permissions on {target}: {exc}", file=sys.stderr)


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    _harden_permissions(DATA_DIR, is_dir=True)


def load_log() -> list[dict[str, Any]]:
    if not LOG_JSON.exists():
        return []
    raw = LOG_JSON.read_text(encoding="utf-8")
    return json.loads(raw) if raw.strip() else []


def _write_csv(entries: list[dict[str, Any]]) -> None:
    with LOG_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for entry in entries:
            writer.writerow({col: entry.get(col, "") for col in CSV_COLUMNS})
    _harden_permissions(LOG_CSV)


def save_log(entries: list[dict[str, Any]]) -> None:
    ensure_data_dir()
    LOG_JSON.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    _harden_permissions(LOG_JSON)
    _write_csv(entries)


def completed_test_ids(entries: list[dict[str, Any]]) -> set[str]:
    return {e["test_id"] for e in entries}


class EngagementStatus:
    def __init__(self, entries: list[dict[str, Any]]):
        self.entries = entries
        self.used = len(entries)
        self.remaining = ENGAGEMENT_BUDGET.total_attempts - self.used
        self.total = ENGAGEMENT_BUDGET.total_attempts
        done = completed_test_ids(entries)
        self.completed = sorted(done)
        self.pending = [t.test_id for t in TEST_SUITE if t.test_id not in done]


def get_status() -> EngagementStatus:
    return EngagementStatus(load_log())


def run_next_test(tester_id: str) -> None:
    """
    Guides one full attempt end-to-end: shows the prompt, logs dispatch
    time on confirmation (spending 1 of 6 attempts), captures the
    response, then asks for observed behavior / risk rating /
    reproducibility notes.
    """
    if tester_id not in ENGAGEMENT_BUDGET.authorized_tester_ids:
        raise ValueError(
            f"Tester ID \"{tester_id}\" is not in the authorized list: "
            f"{', '.join(ENGAGEMENT_BUDGET.authorized_tester_ids)}"
        )

    status = get_status()
    if status.remaining <= 0:
        print("Budget exhausted: all 6 attempts have been used. Run `report_generator.py` to generate findings.")
        return

    if not status.pending:
        print("All tests in the suite have already been completed.")
        return

    next_test_id = status.pending[0]
    test = next(t for t in TEST_SUITE if t.test_id == next_test_id)

    print(f"\n=== {test.test_id} — {test.category} ===")
    print(f"Garak taxonomy analogue: {test.garak_analogue}")
    print(f"Guardrail claim(s) targeted: {'; '.join(test.guardrail_claims_targeted)}")
    print(
        f"\nPrompt to paste into the target chat box "
        f"({len(test.prompt_text)}/{ENGAGEMENT_BUDGET.input_char_limit} chars):\n"
    )
    print(test.prompt_text)

    confirmed = input("\nHave you pasted this prompt into the target chat box? (y/n): ")
    if confirmed.strip().lower() != "y":
        print("Aborted — no attempt was logged, budget unchanged.")
        return

    dispatched_at = datetime.now(timezone.utc).isoformat()

    response_text = input("\nPaste the model's response, then press Enter:\n")
    response_captured_at = datetime.now(timezone.utc).isoformat()
    observed_behavior = input("\nObserved behavior (free text): ")
    risk_rating = input("\nRisk rating (None/Low/Medium/High, with optional rationale): ")
    reproducibility_notes = input("\nReproducibility notes (free text): ")

    entry = {
        "test_id": test.test_id,
        "category": test.category,
        "tester_id": tester_id,
        "prompt_text": test.prompt_text,
        "prompt_char_count": len(test.prompt_text),
        "dispatched_at_utc": dispatched_at,
        "response_text": response_text,
        "response_captured_at_utc": response_captured_at,
        "observed_behavior": observed_behavior,
        "risk_rating": risk_rating,
        "reproducibility_notes": reproducibility_notes,
        "attempt_number": status.used + 1,
    }

    entries = status.entries + [entry]
    save_log(entries)

    print(f"\nLogged {test.test_id}. Attempts used: {len(entries)}/{ENGAGEMENT_BUDGET.total_attempts}.")


def normalize_existing_log() -> int:
    """
    Re-saves the existing JSON log through the same path used by
    interactive logging, which regenerates the CSV mirror and re-applies
    owner-only file permissions. Useful after manually placing/editing
    attempt_log.json (e.g. across multiple stop/start testing sessions).
    """
    entries = load_log()
    save_log(entries)
    return len(entries)
