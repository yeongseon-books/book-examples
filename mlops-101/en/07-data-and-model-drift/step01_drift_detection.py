"""Mlops 101 - Episode 1: Drift detection."""

import numpy as np
from common import DriftDetector


def run_drift_demo() -> dict[str, float | bool]:
    """Run drift demo."""
    rng = np.random.default_rng(42)
    base = rng.normal(0.0, 1.0, 1000)
    live = rng.normal(0.7, 1.0, 1000)
    return DriftDetector().detect(base, live)


if __name__ == "__main__":
    print(run_drift_demo())
