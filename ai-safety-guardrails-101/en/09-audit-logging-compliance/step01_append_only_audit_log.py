"""Ai Safety Guardrails 101 - Episode 9: audit logging compliance example."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import AuditLog


def run() -> dict[str, object]:
    """Run."""
    log = AuditLog()
    log.append("request", "user=demo")
    log.append("decision", "blocked=false")
    return {"count": len(log.records), "chain_ok": log.verify_chain()}


if __name__ == "__main__":
    print(run())
