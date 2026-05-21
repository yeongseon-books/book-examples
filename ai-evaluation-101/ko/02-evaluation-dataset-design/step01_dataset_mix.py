"""Ai Evaluation 101 - 2편: evaluation dataset design 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run() -> dict[str, int]:
    """Run."""
    dataset = [
        {"id": "p1", "category": "happy_path"},
        {"id": "p2", "category": "happy_path"},
        {"id": "e1", "category": "edge_case"},
        {"id": "r1", "category": "regression"},
        {"id": "a1", "category": "adversarial"},
    ]
    counts = {"happy_path": 0, "edge_case": 0, "regression": 0, "adversarial": 0}
    for item in dataset:
        counts[item["category"]] += 1
    return counts


if __name__ == "__main__":
    print(run())
