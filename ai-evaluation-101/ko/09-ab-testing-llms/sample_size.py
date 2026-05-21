# ab/sample_size.py
import statsmodels.stats.power as smp

def required_sample_size(p_a: float, p_b: float,
                          alpha: float = 0.05, power: float = 0.8) -> int:
    """Per-group sample size to detect a difference between two proportions."""
    effect_size = smp.proportion_effectsize(p_a, p_b)
    n = smp.NormalIndPower().solve_power(
        effect_size=abs(effect_size),
        alpha=alpha,
        power=power,
        alternative="two-sided",
    )
    return int(n) + 1

# To detect 60% vs 50%
print(required_sample_size(0.6, 0.5))  # ~388

# 55% vs 50% (small difference)
print(required_sample_size(0.55, 0.5))  # ~1565

# 70% vs 50% (large difference)
print(required_sample_size(0.7, 0.5))  # ~93
