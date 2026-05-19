"""Sre 101 - Episode 10: Operable checklist."""

CHECKS = ["logs", "metrics", "traces", "runbook", "dashboards", "alerts"]


def checklist_score(state: dict[str, bool]) -> tuple[int, float]:
    """Checklist score."""
    passed = sum(1 for k in CHECKS if state.get(k, False))
    return passed, passed / len(CHECKS)
