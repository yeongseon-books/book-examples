"""Math For Cs 101 - Episode 1: Calculus."""

import numpy as np


def trapezoid_integral(f, a, b, n=1000):
    """Trapezoid integral."""
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)
    h = (b - a) / n
    return float(h * (0.5 * ys[0] + ys[1:-1].sum() + 0.5 * ys[-1]))


def simpson_integral(f, a, b, n=1000):
    """Simpson integral."""
    if n % 2 == 1:
        n += 1
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)
    h = (b - a) / n
    return float(
        (h / 3) * (ys[0] + ys[-1] + 4 * ys[1:-1:2].sum() + 2 * ys[2:-2:2].sum())
    )
