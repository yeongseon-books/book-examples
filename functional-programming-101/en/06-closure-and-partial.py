"""Functional Programming 101 - Episode 6: Closure and partial."""

from __future__ import annotations

from collections.abc import Callable
from functools import partial


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Make multiplier."""

    def _mul(value: int) -> int:
        """Mul."""
        return value * factor

    return _mul


def multiply(value: int, factor: int) -> int:
    """Multiply."""
    return value * factor


def times_three() -> Callable[[int], int]:
    """Times three."""
    return partial(multiply, factor=3)


if __name__ == "__main__":
    print(make_multiplier(2)(10), times_three()(10))
