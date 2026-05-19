"""Observability 101 - Episode 6: Dashboard design."""

from common import Dashboard


def run_demo() -> tuple[str, dict[str, float]]:
    """Run demo."""
    values = [0.2, 0.3, 0.5, 0.4, 0.9]
    return Dashboard.sparkline(values), Dashboard.summary(values)
