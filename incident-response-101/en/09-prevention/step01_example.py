"""Incident Response 101 - Episode 9: prevention example."""

from common import PreventionTracker


def run() -> list[dict[str, str]]:
    """Run."""
    tracker = PreventionTracker()
    a1 = tracker.add("add regression for timeout", "backend", "2026-06-01")
    tracker.add("introduce query guardrail", "db-team", "2026-06-05")
    tracker.set_status(a1["id"], "done")
    return tracker.items


if __name__ == "__main__":
    print(run())
