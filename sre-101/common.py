"""Shared utilities and domain models for Sre 101."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Incident:
    """Incident."""

    start_minute: int
    end_minute: int

    @property
    def duration(self) -> int:
        """Duration."""
        return max(0, self.end_minute - self.start_minute)


def ratio(numerator: float, denominator: float) -> float:
    """Ratio."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def percentile(values: Iterable[float], q: float) -> float:
    """Percentile."""
    import numpy as np

    arr = np.array(list(values), dtype=float)
    if arr.size == 0:
        return 0.0
    return float(np.percentile(arr, q))
