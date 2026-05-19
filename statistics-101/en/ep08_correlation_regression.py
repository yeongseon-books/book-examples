from __future__ import annotations

import numpy as np

from common import rng


def run_demo() -> dict[str, float]:
    g = rng()
    x = np.linspace(0, 10, 60)
    y = 1.5 + 2.2 * x + g.normal(0, 1.5, size=x.size)
    r = float(np.corrcoef(x, y)[0, 1])
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    beta1 = float(np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2))
    beta0 = float(y_mean - beta1 * x_mean)
    return {"pearson_r": r, "beta0": beta0, "beta1": beta1}


if __name__ == "__main__":
    print(run_demo())
