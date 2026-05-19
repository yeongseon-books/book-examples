"""Mlops 101 - Episode 1: Model monitoring."""

from common import Monitoring


def run_monitoring_demo() -> float:
    """Run monitoring demo."""
    mon = Monitoring()
    mon.record(1, 10.0, ok=True)
    mon.record(0, 15.0, ok=False)
    mon.record(1, 11.0, ok=True)
    return mon.error_rate()


if __name__ == "__main__":
    print(run_monitoring_demo())
