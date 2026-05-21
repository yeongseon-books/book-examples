"""Generated from book-content article."""

def f(x: float) -> float:
    return (x - 3.0) ** 2 + 2.0


def dfdx(x: float) -> float:
    return 2.0 * (x - 3.0)


def gradient_descent(x0: float, lr: float = 0.1, steps: int = 30) -> float:
    x = x0
    for _ in range(steps):
        x = x - lr * dfdx(x)
    return x
