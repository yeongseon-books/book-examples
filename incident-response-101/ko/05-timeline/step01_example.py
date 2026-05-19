"""Incident Response 101 - Episode 1: Example."""

from common import IncidentTimeline


def run() -> list[dict[str, str]]:
    """Run."""
    tl = IncidentTimeline()
    tl.append("monitor", "detected", "2026-05-01T00:00:00+00:00")
    tl.append("oncall", "acknowledged", "2026-05-01T00:01:00+00:00")
    tl.append("ops", "mitigated", "2026-05-01T00:05:00+00:00")
    return tl.events


if __name__ == "__main__":
    print(run())
