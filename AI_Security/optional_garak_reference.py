"""
optional_garak_reference.py

Offline-only mapping of each test category to Garak's published probe
taxonomy, for documentation / cross-referencing purposes. No live Garak
execution happens here or anywhere in this toolkit — Garak's automated,
high-volume probing model doesn't fit a 6-attempt manual engagement
against a no-API web chat box.

Garak is optional: if the `garak` package happens to be installed in a
sibling environment, a human reviewer can independently look up these
probe names in Garak's own docs. This module does not import garak and
has zero runtime dependency on it.
"""

from __future__ import annotations

GARAK_TAXONOMY_REFERENCE: dict[str, dict[str, str]] = {
    "system_prompt_disclosure": {
        "probes": "garak.probes.promptinject / garak.probes.leakreplay",
        "note": (
            "Direct/instructed attempts to make the target reveal its "
            "system prompt or hidden instructions."
        ),
    },
    "instruction_override": {
        "probes": "garak.probes.promptinject / garak.probes.dan",
        "note": (
            "Role-override and 'DAN'-style jailbreak probe family; "
            "fabricated authority/mode claims intended to supersede prior "
            "rules."
        ),
    },
    "policy_bypass": {
        "probes": "garak.probes.encoding / garak.probes.malwaregen",
        "note": (
            "Smuggling disallowed content inside an otherwise-allowed "
            "context (e.g. requesting code via an in-scope framing)."
        ),
    },
    "indirect_prompt_injection_simulation": {
        "probes": "garak.probes.latentinjection",
        "note": (
            "Instructions embedded in quoted/pasted third-party content "
            "rather than stated directly by the user."
        ),
    },
    "output_constraint_test": {
        "probes": "garak.probes.continuation",
        "note": (
            "Whether stated output limits (length, format) are enforced "
            "server-side or are only soft model-level instructions."
        ),
    },
    "direct_prompt_injection": {
        "probes": "garak.probes.promptinject",
        "note": (
            "Forged-authority / compound override attempts bundling "
            "multiple asks (disclosure + rate-limit bypass + acceptance)."
        ),
    },
}


def lookup_garak_reference(category: str) -> dict[str, str] | None:
    """Look up the Garak taxonomy reference for a given test category.
    Returns None if no offline mapping exists for that category."""
    return GARAK_TAXONOMY_REFERENCE.get(category)
