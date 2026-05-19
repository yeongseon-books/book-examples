"""Functional Programming 101 - Episode 5: Map filter reduce."""

from __future__ import annotations

from functools import reduce


def map_filter_reduce_total(values: list[int]) -> int:
    """Map filter reduce total."""
    mapped = map(lambda x: x * 2, values)
    filtered = filter(lambda x: x % 3 == 0, mapped)
    return reduce(lambda acc, x: acc + x, filtered, 0)


def comprehension_total(values: list[int]) -> int:
    """Comprehension total."""
    return sum(x * 2 for x in values if (x * 2) % 3 == 0)


if __name__ == "__main__":
    print(map_filter_reduce_total([1, 2, 3, 4, 5, 6]))
