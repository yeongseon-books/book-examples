# ab/significance.py
from statsmodels.stats.proportion import proportions_ztest

def is_significantly_better(wins_a: int, wins_b: int,
                              total: int, alpha: float = 0.05) -> dict:
    # Drop ties from the denominator; compare wins_a vs wins_b
    n_decisive = wins_a + wins_b
    if n_decisive == 0:
        return {"significant": False, "p_value": 1.0, "winner": None}

    count = [wins_a, wins_b]
    nobs = [n_decisive, n_decisive]
    z_stat, p_value = proportions_ztest(count, nobs)

    return {
        "p_value":     p_value,
        "significant": p_value < alpha,
        "winner":      "A" if wins_a > wins_b else "B",
        "win_rate_a":  wins_a / n_decisive,
        "win_rate_b":  wins_b / n_decisive,
    }

print(is_significantly_better(wins_a=240, wins_b=160, total=400))
# {'p_value': 0.0001, 'significant': True, 'winner': 'A', 'win_rate_a': 0.6, ...}

print(is_significantly_better(wins_a=22, wins_b=18, total=40))
# {'p_value': 0.52, 'significant': False, 'winner': 'A', ...}
# Same 60% vs 45% but the sample is too small
