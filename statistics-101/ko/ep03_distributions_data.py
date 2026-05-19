from __future__ import annotations

import numpy as np
from scipy import stats


def run_demo() -> dict[str, np.ndarray]:
    x = np.linspace(-3.0, 3.0, 121)
    normal_pdf = stats.norm.pdf(x, loc=0.0, scale=1.0)
    k_binom = np.arange(0, 11)
    binom_pmf = stats.binom.pmf(k_binom, n=10, p=0.3)
    k_poisson = np.arange(0, 16)
    poisson_pmf = stats.poisson.pmf(k_poisson, mu=4.0)
    x_exp = np.linspace(0.0, 5.0, 101)
    exp_pdf = stats.expon.pdf(x_exp, scale=1.0)
    return {
        "x_normal": x,
        "normal_pdf": normal_pdf,
        "k_binom": k_binom,
        "binom_pmf": binom_pmf,
        "k_poisson": k_poisson,
        "poisson_pmf": poisson_pmf,
        "x_exp": x_exp,
        "exp_pdf": exp_pdf,
    }


if __name__ == "__main__":
    out = run_demo()
    print({k: v.shape for k, v in out.items()})
