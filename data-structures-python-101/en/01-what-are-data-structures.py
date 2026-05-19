"""Data Structures Python 101 - Episode 1: What are data structures."""

from collections import Counter
from collections.abc import Callable
from time import perf_counter
from typing import Any


def time_op(
    fn: Callable[..., Any], *args: Any, repeat: int = 5, loops: int = 1, **kwargs: Any
) -> float:
    """Time op."""
    best = float("inf")
    for _ in range(repeat):
        start = perf_counter()
        for _ in range(loops):
            fn(*args, **kwargs)
        best = min(best, perf_counter() - start)
    return best


TEXT = "python data structures with python data"


def words_from_text(text: str) -> list[str]:
    """Words from text."""
    return text.split()


def count_with_list(words: list[str]) -> dict[str, int]:
    """Count with list."""
    uniq = sorted(set(words))
    return {w: words.count(w) for w in uniq}


def count_with_dict(words: list[str]) -> dict[str, int]:
    """Count with dict."""
    out: dict[str, int] = {}
    for w in words:
        out[w] = out.get(w, 0) + 1
    return out


def count_with_counter(words: list[str]) -> dict[str, int]:
    """Count with counter."""
    return dict(Counter(words))


def benchmark_counts(words: list[str]) -> dict[str, float]:
    """Benchmark counts."""
    return {
        "list+count": time_op(count_with_list, words, loops=200),
        "dict": time_op(count_with_dict, words, loops=200),
        "Counter": time_op(count_with_counter, words, loops=200),
    }


if __name__ == "__main__":
    words = words_from_text(TEXT)
    print(count_with_counter(words))
    print(benchmark_counts(words))
