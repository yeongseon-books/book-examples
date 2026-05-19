from __future__ import annotations

import numpy as np
from scipy import stats

from common import rng


def run_demo() -> dict[str, float]:
    g = rng()
    true_mean = 10.0
    sigma = 3.0
    n = 40
    sample = g.normal(true_mean, sigma, size=n)
    x_bar = float(np.mean(sample))
    s = float(np.std(sample, ddof=1))
    z = stats.norm.ppf(0.975)
    t = stats.t.ppf(0.975, df=n - 1)
    z_margin = float(z * sigma / np.sqrt(n))
    t_margin = float(t * s / np.sqrt(n))
    z_ci = (x_bar - z_margin, x_bar + z_margin)
    t_ci = (x_bar - t_margin, x_bar + t_margin)

    sims = 1000
    covered = 0
    for _ in range(sims):
        x = g.normal(true_mean, sigma, size=n)
        xb = float(np.mean(x))
        xs = float(np.std(x, ddof=1))
        tm = float(t * xs / np.sqrt(n))
        if xb - tm <= true_mean <= xb + tm:
            covered += 1
    coverage = covered / sims
    return {
        "z_ci_low": z_ci[0],
        "z_ci_high": z_ci[1],
        "t_ci_low": t_ci[0],
        "t_ci_high": t_ci[1],
        "coverage": float(coverage),
    }


if __name__ == "__main__":
    print(run_demo())
