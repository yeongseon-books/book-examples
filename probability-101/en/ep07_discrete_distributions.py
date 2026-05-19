from __future__ import annotations

from scipy.stats import bernoulli, binom, geom, poisson


def run() -> dict[str, float]:
    return {
        "bernoulli_pmf_1": float(bernoulli.pmf(1, 0.3)),
        "binom_pmf_3": float(binom.pmf(3, 10, 0.4)),
        "poisson_pmf_2": float(poisson.pmf(2, 1.5)),
        "geom_pmf_4": float(geom.pmf(4, 0.2)),
    }


if __name__ == "__main__":
    print(run())
