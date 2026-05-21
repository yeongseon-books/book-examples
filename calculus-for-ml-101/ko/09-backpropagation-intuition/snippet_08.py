"""Generated from book-content article."""

import math


def f(x):
    return math.sin(3 * x + 1)

def analytic_grad(x):
    # d/dx sin(3x+1) = cos(3x+1) * 3
    return math.cos(3 * x + 1) * 3

def numeric_grad(fn, x, h=1e-5):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 0.7
print(analytic_grad(x), numeric_grad(f, x))
