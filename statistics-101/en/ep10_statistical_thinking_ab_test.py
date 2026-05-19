"""Statistics 101 - Episode 10: Statistical thinking ab test."""

from __future__ import annotations

import numpy as np
from common import rng
from scipy import stats


def sample_size_two_proportions(
    p1: float, p2: float, alpha: float = 0.05, power: float = 0.8
) -> int:
    """Sample size two proportions."""
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    p_bar = 0.5 * (p1 + p2)
    num = z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * np.sqrt(
        p1 * (1 - p1) + p2 * (1 - p2)
    )
    den = abs(p2 - p1)
    return int(np.ceil((num / den) ** 2))


def run_demo() -> dict[str, float]:
    """Run demo."""
    g = rng()
    p_control = 0.10
    p_variant = 0.12
    n = sample_size_two_proportions(p_control, p_variant)

    control = g.binomial(1, p_control, size=n)
    variant = g.binomial(1, p_variant, size=n)
    c_rate = float(np.mean(control))
    v_rate = float(np.mean(variant))

    pooled = (np.sum(control) + np.sum(variant)) / (2 * n)
    se = np.sqrt(pooled * (1 - pooled) * (2 / n))
    z = (v_rate - c_rate) / se
    p_value = float(2 * (1 - stats.norm.cdf(abs(z))))

    return {
        "recommended_n_per_group": float(n),
        "control_rate": c_rate,
        "variant_rate": v_rate,
        "lift": v_rate - c_rate,
        "p_value": p_value,
    }


if __name__ == "__main__":
    print(run_demo())
