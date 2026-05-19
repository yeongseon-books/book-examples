"""Software Engineering 101 - Episode 8: Collab."""

from __future__ import annotations

import csv
from io import StringIO


def raci_matrix_validator(csv_text: str) -> dict[str, object]:
    """Raci matrix validator."""
    reader = csv.DictReader(StringIO(csv_text))
    rows = list(reader)
    valid = True
    errors = []
    for idx, row in enumerate(rows, start=1):
        if not row.get("responsible") or not row.get("accountable"):
            valid = False
            errors.append(f"row {idx} missing responsible/accountable")
    return {"valid": valid, "rows": len(rows), "errors": errors}


def standup_notes_parser(text: str) -> dict[str, str]:
    """Standup notes parser."""
    out = {"yesterday": "", "today": "", "blockers": ""}
    for line in text.splitlines():
        lower = line.lower()
        if lower.startswith("yesterday:"):
            out["yesterday"] = line.split(":", 1)[1].strip()
        elif lower.startswith("today:"):
            out["today"] = line.split(":", 1)[1].strip()
        elif lower.startswith("blockers:"):
            out["blockers"] = line.split(":", 1)[1].strip()
    return out
