"""Mlops 101 - Episode 1: Experiment tracking."""

from common import ExperimentTracker


def run_tracking_demo() -> str:
    """Run tracking demo."""
    tracker = ExperimentTracker()
    tracker.log_run({"C": 0.1}, {"accuracy": 0.81}, {"model": "m1"})
    tracker.log_run({"C": 1.0}, {"accuracy": 0.88}, {"model": "m2"})
    return tracker.best_run("accuracy")["run_id"]


if __name__ == "__main__":
    print(run_tracking_demo())
