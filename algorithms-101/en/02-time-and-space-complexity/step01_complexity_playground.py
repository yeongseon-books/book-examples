"""Algorithms 101 - Episode 1: Complexity playground."""

from __future__ import annotations

from common import make_random_list, measure_ms


def linear_sum(values: list[int]) -> int:
    """Linear sum."""
    total = 0
    for v in values:
        total += v
    return total


def quadratic_pair_count(values: list[int]) -> int:
    """Quadratic pair count."""
    count = 0
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] <= values[j]:
                count += 1
    return count


def run() -> dict[str, float]:
    """Run."""
    a = make_random_list(3000, seed=7)
    b = make_random_list(700, seed=7)
    return {
        "linear_ms": measure_ms(lambda: linear_sum(a)),
        "quadratic_ms": measure_ms(lambda: quadratic_pair_count(b)),
    }


if __name__ == "__main__":
    print(run())
