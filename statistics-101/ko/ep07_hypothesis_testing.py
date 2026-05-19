from __future__ import annotations

import numpy as np
from common import rng
from scipy import stats


def run_demo() -> dict[str, float]:
    g = rng()
    x = g.normal(51, 10, size=30)
    n1 = x.size
    m1 = float(np.mean(x))
    s1 = float(np.std(x, ddof=1))
    t1 = (m1 - 50.0) / (s1 / np.sqrt(n1))
    p1 = float(2 * (1 - stats.t.cdf(abs(t1), df=n1 - 1)))

    a = g.normal(100, 12, size=35)
    b = g.normal(104, 12, size=33)
    n_a = a.size
    n_b = b.size
    m_a = float(np.mean(a))
    m_b = float(np.mean(b))
    v_a = float(np.var(a, ddof=1))
    v_b = float(np.var(b, ddof=1))
    se = np.sqrt(v_a / n_a + v_b / n_b)
    t2 = (m_a - m_b) / se
    df_num = (v_a / n_a + v_b / n_b) ** 2
    df_den = (v_a**2) / ((n_a**2) * (n_a - 1)) + (v_b**2) / ((n_b**2) * (n_b - 1))
    df = df_num / df_den
    p2 = float(2 * (1 - stats.t.cdf(abs(t2), df=df)))

    observed = np.array([18, 22, 20])
    expected = np.array([20, 20, 20])
    chi2 = float(np.sum((observed - expected) ** 2 / expected))
    p3 = float(1 - stats.chi2.cdf(chi2, df=2))

    return {
        "one_sample_t": float(t1),
        "one_sample_p": p1,
        "two_sample_t": float(t2),
        "two_sample_p": p2,
        "chi2_stat": chi2,
        "chi2_p": p3,
    }


if __name__ == "__main__":
    print(run_demo())
