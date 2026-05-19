"""Shared utilities and domain models for Algorithms Python 101."""

from __future__ import annotations

from collections.abc import Callable
from time import perf_counter


def measure(func: Callable[..., object], *args: object, repeat: int = 3) -> float:
    """Measure."""
    best = float("inf")
    for _ in range(repeat):
        start = perf_counter()
        _ = func(*args)
        elapsed = perf_counter() - start
        if elapsed < best:
            best = elapsed
    return best
