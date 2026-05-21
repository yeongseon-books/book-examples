"""Math For Cs 101 - Episode 6: probability example."""

import random


def estimate_pi(n=100000, seed=7):
    """Estimate pi."""
    rnd = random.Random(seed)
    inside = 0
    for _ in range(n):
        x, y = rnd.random(), rnd.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4.0 * inside / n


def bayes(p_b_given_a, p_a, p_b):
    """Bayes."""
    return p_b_given_a * p_a / p_b


def expected_value(values, probs):
    """Expected value."""
    return sum(v * p for v, p in zip(values, probs, strict=False))
