"""Computer Architecture 101 - Episode 10: Understanding performance."""

from __future__ import annotations

import timeit


def amdahl(p: float, n: int) -> float:
    """Amdahl."""
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be between 0 and 1")
    if n <= 0:
        raise ValueError("n must be positive")
    return 1.0 / ((1.0 - p) + (p / n))


def loop_impl() -> int:
    """Loop impl."""
    total = 0
    for i in range(1000):
        total += i * i
    return total


def comprehension_impl() -> int:
    """Comprehension impl."""
    return sum(i * i for i in range(1000))


def benchmark() -> dict[str, float]:
    """Benchmark."""
    t_loop = timeit.timeit(loop_impl, number=200)
    t_comp = timeit.timeit(comprehension_impl, number=200)
    return {"loop": t_loop, "comprehension": t_comp}


if __name__ == "__main__":
    print(amdahl(0.9, 4))
    print(benchmark())
