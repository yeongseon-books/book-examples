from __future__ import annotations

import numpy as np

from common import make_rng


def run(n: int = 200_000) -> dict[str, float]:
    values = np.array([0, 1, 2, 3])
    probs = np.array([0.1, 0.2, 0.4, 0.3])
    rng = make_rng()
    samples = rng.choice(values, size=n, p=probs)
    empirical_mean = float(samples.mean())
    exact_mean = float((values * probs).sum())
    return {
        "exact_mean": exact_mean,
        "empirical_mean": empirical_mean,
        "pmf_sum": float(probs.sum()),
    }


if __name__ == "__main__":
    print(run())
