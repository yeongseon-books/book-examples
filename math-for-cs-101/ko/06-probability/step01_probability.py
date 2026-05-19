import random


def estimate_pi(n=100000, seed=7):
    rnd = random.Random(seed)
    inside = 0
    for _ in range(n):
        x, y = rnd.random(), rnd.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4.0 * inside / n


def bayes(p_b_given_a, p_a, p_b):
    return p_b_given_a * p_a / p_b


def expected_value(values, probs):
    return sum(v * p for v, p in zip(values, probs))
