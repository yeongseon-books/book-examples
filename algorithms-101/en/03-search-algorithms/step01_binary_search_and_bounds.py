"""Algorithms 101 - Episode 1: Binary search and bounds."""

from __future__ import annotations

import bisect


def lower_bound(arr: list[int], target: int) -> int:
    """Lower bound."""
    return bisect.bisect_left(arr, target)


def upper_bound(arr: list[int], target: int) -> int:
    """Upper bound."""
    return bisect.bisect_right(arr, target)


def count_occurrence(arr: list[int], target: int) -> int:
    """Count occurrence."""
    return upper_bound(arr, target) - lower_bound(arr, target)


def run() -> dict[str, object]:
    """Run."""
    arr = [1, 2, 2, 2, 3, 4, 5]
    return {
        "arr": arr,
        "lb": lower_bound(arr, 2),
        "ub": upper_bound(arr, 2),
        "count": count_occurrence(arr, 2),
    }


if __name__ == "__main__":
    print(run())
