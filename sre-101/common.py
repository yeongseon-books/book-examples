from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Incident:
    start_minute: int
    end_minute: int

    @property
    def duration(self) -> int:
        return max(0, self.end_minute - self.start_minute)


def ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def percentile(values: Iterable[float], q: float) -> float:
    import numpy as np

    arr = np.array(list(values), dtype=float)
    if arr.size == 0:
        return 0.0
    return float(np.percentile(arr, q))
