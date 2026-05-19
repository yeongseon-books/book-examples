"""Observability 101 - Episode 8: Sli and slo."""

from common import SLOTracker


def run_demo() -> tuple[float, float, float]:
    """Run demo."""
    tracker = SLOTracker(target=0.999)
    tracker.record(9980, 10000)
    return tracker.sli(), tracker.error_budget_remaining(), tracker.burn_rate()
