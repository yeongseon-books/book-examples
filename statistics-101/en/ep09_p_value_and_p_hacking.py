from __future__ import annotations

import numpy as np
from scipy import stats

from common import rng


def run_demo() -> dict[str, float]:
    g = rng()
    baseline = g.normal(0, 1, size=40)
    variant = g.normal(0.3, 1, size=40)
    n1 = baseline.size
    n2 = variant.size
    m1 = float(np.mean(baseline))
    m2 = float(np.mean(variant))
    v1 = float(np.var(baseline, ddof=1))
    v2 = float(np.var(variant, ddof=1))
    se = np.sqrt(v1 / n1 + v2 / n2)
    t = (m1 - m2) / se
    df_num = (v1 / n1 + v2 / n2) ** 2
    df_den = (v1**2) / ((n1**2) * (n1 - 1)) + (v2**2) / ((n2**2) * (n2 - 1))
    df = df_num / df_den
    single_test_p = float(2 * (1 - stats.t.cdf(abs(t), df=df)))

    n_tests = 20
    raw_ps = []
    for _ in range(n_tests):
        a = g.normal(0, 1, size=25)
        b = g.normal(0, 1, size=25)
        na = a.size
        nb = b.size
        ma = float(np.mean(a))
        mb = float(np.mean(b))
        va = float(np.var(a, ddof=1))
        vb = float(np.var(b, ddof=1))
        se_ab = np.sqrt(va / na + vb / nb)
        t_ab = (ma - mb) / se_ab
        df_num_ab = (va / na + vb / nb) ** 2
        df_den_ab = (va**2) / ((na**2) * (na - 1)) + (vb**2) / ((nb**2) * (nb - 1))
        df_ab = df_num_ab / df_den_ab
        p = float(2 * (1 - stats.t.cdf(abs(t_ab), df=df_ab)))
        raw_ps.append(p)
    min_p = float(np.min(raw_ps))
    bonf_min_p = float(min(min_p * n_tests, 1.0))

    return {
        "single_test_p": single_test_p,
        "min_raw_p": min_p,
        "min_bonferroni_p": bonf_min_p,
        "num_tests": float(n_tests),
    }


if __name__ == "__main__":
    print(run_demo())
