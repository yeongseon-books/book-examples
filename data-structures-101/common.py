"""Shared utilities and domain models for Data Structures 101."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from time import perf_counter
from typing import Any


@dataclass
class Node:
    """Node."""

    value: Any
    next: Any = None
    prev: Any = None


class OperationCounter:
    """Operation counter."""

    def __init__(self) -> None:
        self.counts: dict[str, int] = {}

    def inc(self, key: str, amount: int = 1) -> None:
        """Inc."""
        self.counts[key] = self.counts.get(key, 0) + amount

    def get(self, key: str) -> int:
        """Get."""
        return self.counts.get(key, 0)

    def total(self) -> int:
        """Total."""
        return sum(self.counts.values())


def time_op(fn: Callable[[], Any]) -> tuple[Any, float]:
    """Time op."""
    start = perf_counter()
    value = fn()
    return value, perf_counter() - start
