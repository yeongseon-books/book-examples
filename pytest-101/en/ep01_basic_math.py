"""Pytest 101 - Episode 1: Basic math."""


def add(a: int, b: int) -> int:
    """Add."""
    return a + b


def factorial(n: int) -> int:
    """Factorial."""
    if n < 0:
        raise ValueError("n must be non-negative")
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out
