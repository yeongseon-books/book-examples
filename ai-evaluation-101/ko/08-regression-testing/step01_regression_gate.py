"""Ai Evaluation 101 - Episode 1: Regression gate."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run() -> dict[str, object]:
    """Run."""
    current = {"exact_match": 0.84, "faithfulness": 0.88, "task_success": 0.91}
    thresholds = {"exact_match": 0.8, "faithfulness": 0.85, "task_success": 0.9}
    failed = [
        name for name, threshold in thresholds.items() if current[name] < threshold
    ]
    return {"failed": failed, "passed": len(failed) == 0}


if __name__ == "__main__":
    print(run())
