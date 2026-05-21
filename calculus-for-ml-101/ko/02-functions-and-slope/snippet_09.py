"""Generated from book-content article."""

import time


def measure(fn, *args, repeat=3):
    best = float('inf')
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn(*args)
        best = min(best, time.perf_counter() - t0)
    return best
