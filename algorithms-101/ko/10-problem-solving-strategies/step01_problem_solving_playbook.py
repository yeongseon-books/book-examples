"""Algorithms 101 - Episode 1: Problem solving playbook."""

from __future__ import annotations


def max_subarray(arr: list[int]) -> int:
    """Max subarray."""
    if not arr:
        return 0
    cur = best = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def run() -> dict[str, object]:
    """Run."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    return {"arr": arr, "best": max_subarray(arr)}


if __name__ == "__main__":
    print(run())
