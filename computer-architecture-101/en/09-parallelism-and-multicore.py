"""Computer Architecture 101 - Episode 9: Parallelism and multicore."""

from __future__ import annotations

import threading
import time


def vector_add_sequential(a: list[int], b: list[int]) -> list[int]:
    """Vector add sequential."""
    return [x + y for x, y in zip(a, b, strict=False)]


def vector_add_threaded(a: list[int], b: list[int], workers: int = 4) -> list[int]:
    """Vector add threaded."""
    out = [0] * len(a)
    chunk = max(1, len(a) // workers)
    threads: list[threading.Thread] = []

    def worker(start: int, end: int) -> None:
        """Worker."""
        for i in range(start, end):
            out[i] = a[i] + b[i]

    for w in range(workers):
        start = w * chunk
        end = len(a) if w == workers - 1 else min(len(a), (w + 1) * chunk)
        t = threading.Thread(target=worker, args=(start, end))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return out


def measure_speedup(size: int = 200_000) -> dict[str, float]:
    """Measure speedup."""
    a = list(range(size))
    b = list(range(size, 2 * size))
    t0 = time.perf_counter()
    seq = vector_add_sequential(a, b)
    seq_t = time.perf_counter() - t0
    t1 = time.perf_counter()
    par = vector_add_threaded(a, b)
    par_t = time.perf_counter() - t1
    assert seq == par
    return {
        "sequential": seq_t,
        "threaded": par_t,
        "speedup": seq_t / par_t if par_t else 0.0,
    }


if __name__ == "__main__":
    print(measure_speedup())
