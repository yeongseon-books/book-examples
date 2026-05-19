"""Functional Programming 101 - Episode 9: Function composition."""

from __future__ import annotations

from common import compose


def f(x: int) -> int:
    """F."""
    return x + 1


def g(x: int) -> int:
    """G."""
    return x * 2


def h(x: int) -> int:
    """H."""
    return x - 3


def composed_value(x: int) -> int:
    """Composed value."""
    return compose(f, g, h)(x)


if __name__ == "__main__":
    print(composed_value(10))
