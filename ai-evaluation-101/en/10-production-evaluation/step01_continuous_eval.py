"""Ai Evaluation 101 - Episode 10: production evaluation example."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run() -> dict[str, float | bool]:
    """Run."""
    baseline_thumbs_down = 0.03
    baseline_std = 0.005
    today_thumbs_down = 0.047
    z_gap = abs(today_thumbs_down - baseline_thumbs_down) / baseline_std
    drift_alert = z_gap >= 3.0
    return {
        "today_thumbs_down": today_thumbs_down,
        "z_gap": z_gap,
        "drift_alert": drift_alert,
    }


if __name__ == "__main__":
    print(run())
