def numerical_partial(func, x: list[float], i: int, h: float = 1e-5) -> float:
    xp = x.copy()
    xm = x.copy()
    xp[i] += h
    xm[i] -= h
    return (func(xp) - func(xm)) / (2 * h)


def f(x: list[float]) -> float:
    return x[0] ** 2 + 3 * x[1]


def partials(x: list[float]) -> tuple[float, float]:
    return numerical_partial(f, x, 0), numerical_partial(f, x, 1)


def run_demo() -> dict[str, tuple[float, float]]:
    return {"partials_at_2_1": partials([2.0, 1.0])}
