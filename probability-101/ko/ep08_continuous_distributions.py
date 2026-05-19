from __future__ import annotations

import numpy as np
from common import make_rng
from scipy.stats import expon, norm, uniform


def run(n: int = 100_000) -> dict[str, float]:
    rng = make_rng()
    normal_samples = np.asarray(
        norm.rvs(loc=0, scale=1, size=n, random_state=rng), dtype=float
    )
    exp_samples = np.asarray(
        expon.rvs(scale=2.0, size=n, random_state=rng), dtype=float
    )
    uni_samples = np.asarray(
        uniform.rvs(loc=-1, scale=2, size=n, random_state=rng), dtype=float
    )
    return {
        "normal_pdf_0": float(norm.pdf(0)),
        "normal_cdf_0": float(norm.cdf(0)),
        "exp_cdf_1": float(expon.cdf(1, scale=2.0)),
        "uniform_pdf_0": float(uniform.pdf(0, loc=-1, scale=2)),
        "normal_sample_mean": float(normal_samples.mean()),
        "exp_sample_mean": float(exp_samples.mean()),
        "uniform_sample_mean": float(uni_samples.mean()),
    }


if __name__ == "__main__":
    print(run())
