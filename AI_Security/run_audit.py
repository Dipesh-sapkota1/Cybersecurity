#!/usr/bin/env python3
"""
run_audit.py

CLI entry point: `status` / `next` / `normalize` / `report`.

Usage:
    python3 run_audit.py status
    python3 run_audit.py next --tester-id T01
    python3 run_audit.py normalize
    python3 run_audit.py report

Note: if `report` ever fails to see attempts that you know are logged
(e.g. after running `next` across multiple separate stop/start sessions),
run report_generator.py directly against engagement_data/attempt_log.json
instead — it has no dependency on this script's session state and will
always reflect exactly what's in the JSON file on disk:

    python3 report_generator.py engagement_data/attempt_log.json
"""

from __future__ import annotations

import argparse
import sys

from audit_config import ENGAGEMENT_BUDGET
from audit_engine import get_status, run_next_test, normalize_existing_log
from report_generator import generate_report


def print_status() -> None:
    status = get_status()
    print(f"Attempts used: {status.used} / {status.total} ({status.remaining} remaining)")
    print(f"Authorized testers: {', '.join(ENGAGEMENT_BUDGET.authorized_tester_ids)}")
    print(f"Completed tests: {', '.join(status.completed) if status.completed else '(none yet)'}")
    print(f"Pending tests: {', '.join(status.pending) if status.pending else '(all complete)'}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="run_audit.py")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show budget and pending tests")

    next_parser = subparsers.add_parser("next", help="Run the next pending test, guided end-to-end")
    next_parser.add_argument("--tester-id", required=True, help="T01 or T02")

    subparsers.add_parser(
        "normalize",
        help="Regenerate CSV + harden permissions on an existing JSON log",
    )

    subparsers.add_parser("report", help="Generate the Markdown findings report")

    args = parser.parse_args()

    if args.command == "status":
        print_status()
    elif args.command == "next":
        try:
            run_next_test(args.tester_id)
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "normalize":
        count = normalize_existing_log()
        print(f"Normalized {count} entries — CSV regenerated, file permissions hardened to owner-only.")
    elif args.command == "report":
        report_path = generate_report()
        print(f"Report written to: {report_path}")
    else:
        parser.print_help()
        sys.exit(1 if args.command else 0)


if __name__ == "__main__":
    main()
