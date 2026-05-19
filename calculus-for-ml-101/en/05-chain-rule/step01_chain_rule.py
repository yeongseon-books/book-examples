def numerical_derivative_1d(func, x: float, h: float = 1e-5) -> float:
    return (func(x + h) - func(x - h)) / (2 * h)


def g(x: float) -> float:
    return 2 * x + 1


def f(u: float) -> float:
    return u**2


def h(x: float) -> float:
    return f(g(x))


def dh_chain(x: float) -> float:
    return 2 * g(x) * 2


def run_demo() -> dict[str, float]:
    x = 1.0
    return {"chain": dh_chain(x), "numeric": numerical_derivative_1d(h, x)}
