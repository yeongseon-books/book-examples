from common import SLOTracker


def run_demo() -> tuple[float, float, float]:
    tracker = SLOTracker(target=0.999)
    tracker.record(9980, 10000)
    return tracker.sli(), tracker.error_budget_remaining(), tracker.burn_rate()
