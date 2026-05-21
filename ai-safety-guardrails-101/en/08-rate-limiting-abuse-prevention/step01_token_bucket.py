"""Ai Safety Guardrails 101 - Episode 8: rate limiting abuse prevention example."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import TokenBucket


def run(costs: list[int]) -> list[bool]:
    """Run."""
    limiter = TokenBucket(capacity=5, refill_per_sec=0.0)
    return [limiter.allow(cost=c) for c in costs]


if __name__ == "__main__":
    print(run([1, 1, 1, 1, 1, 1]))
