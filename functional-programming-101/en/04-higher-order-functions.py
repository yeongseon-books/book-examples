from __future__ import annotations

from collections.abc import Callable


def apply_to_items(values: list[int], fn: Callable[[int], int]) -> list[int]:
    return [fn(v) for v in values]


def make_threshold_filter(threshold: int) -> Callable[[list[int]], list[int]]:
    return lambda values: [v for v in values if v >= threshold]


if __name__ == "__main__":
    print(apply_to_items([1, 2, 3], lambda x: x * 10))
