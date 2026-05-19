from __future__ import annotations

import numpy as np
from common import rng


def run_demo() -> dict[str, float]:
    g = rng()
    population = np.arange(1, 101, dtype=float)
    sample = g.choice(population, size=20, replace=False)
    return {
        "population_mean": float(np.mean(population)),
        "population_var": float(np.var(population)),
        "sample_mean": float(np.mean(sample)),
        "sample_var_unbiased": float(np.var(sample, ddof=1)),
    }


if __name__ == "__main__":
    print(run_demo())
