"""Probability 101 - Episode 9: Lln clt."""

from __future__ import annotations

import numpy as np
from common import make_rng


def run(rep: int = 20_000, n: int = 36) -> dict[str, float]:
    """Run."""
    rng = make_rng()
    die = rng.integers(1, 7, size=(rep, n))
    sample_means = die.mean(axis=1)
    expected = 3.5
    sigma = np.sqrt(35 / 12)
    clt_std = sigma / np.sqrt(n)
    return {
        "sample_mean_of_means": float(sample_means.mean()),
        "expected": expected,
        "sample_mean_std": float(sample_means.std()),
        "clt_std": float(clt_std),
    }


if __name__ == "__main__":
    print(run())
