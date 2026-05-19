"""Ai Data Preparation 101 - Episode 1: Regex redaction."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import redact_pii


def run() -> dict[str, str]:
    """Run."""
    raw = "문의: alice@example.com, 010-1234-5678"
    redacted = redact_pii(raw)
    return {"raw": raw, "redacted": redacted}


if __name__ == "__main__":
    print(run())
