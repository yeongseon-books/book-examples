"""Calculus For Ml 101 - Episode 1: Chain rule."""


def numerical_derivative_1d(func, x: float, h: float = 1e-5) -> float:
    """Numerical derivative 1d."""
    return (func(x + h) - func(x - h)) / (2 * h)


def g(x: float) -> float:
    """G."""
    return 2 * x + 1


def f(u: float) -> float:
    """F."""
    return u**2


def h(x: float) -> float:
    """H."""
    return f(g(x))


def dh_chain(x: float) -> float:
    """Dh chain."""
    return 2 * g(x) * 2


def run_demo() -> dict[str, float]:
    """Run demo."""
    x = 1.0
    return {"chain": dh_chain(x), "numeric": numerical_derivative_1d(h, x)}
