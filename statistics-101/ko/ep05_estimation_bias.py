from __future__ import annotations

import numpy as np
from common import rng


def run_demo() -> dict[str, float]:
    g = rng()
    true_mean = 5.0
    n = 30
    sims = 2000
    means = np.array([np.mean(g.normal(true_mean, 2.0, size=n)) for _ in range(sims)])
    mle_mean = float(np.mean(g.normal(true_mean, 2.0, size=n)))
    bias = float(np.mean(means) - true_mean)
    return {"true_mean": true_mean, "mle_mean": mle_mean, "estimated_bias": bias}


if __name__ == "__main__":
    print(run_demo())
