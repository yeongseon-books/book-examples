from __future__ import annotations

import random
import time
from collections.abc import Callable


def measure_ms(fn: Callable[[], object]) -> float:
    start = time.perf_counter()
    _ = fn()
    return (time.perf_counter() - start) * 1000


def make_random_list(
    size: int, seed: int = 42, lo: int = -1000, hi: int = 1000
) -> list[int]:
    rng = random.Random(seed)
    return [rng.randint(lo, hi) for _ in range(size)]


def is_sorted_non_decreasing(values: list[int]) -> bool:
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))
