"""Probability 101 - Episode 2: Sample space."""

from __future__ import annotations

from itertools import product


def run() -> dict[str, float]:
    """Run."""
    omega = list(product(range(1, 7), repeat=2))
    p_sum_7 = sum(1 for a, b in omega if a + b == 7) / len(omega)
    p_double = sum(1 for a, b in omega if a == b) / len(omega)
    return {
        "sample_space_size": float(len(omega)),
        "p_sum_7": p_sum_7,
        "p_double": p_double,
    }


if __name__ == "__main__":
    print(run())
