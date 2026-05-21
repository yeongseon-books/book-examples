"""Calculus For Ml 101 - 1편: what is derivative 예제."""


def numerical_derivative_1d(func, x: float, h: float = 1e-5) -> float:
    """Numerical derivative 1d."""
    return (func(x + h) - func(x - h)) / (2 * h)


def square(x: float) -> float:
    """Square."""
    return x**2


def run_demo() -> dict[str, float]:
    """데모를 실행합니다."""
    slope_at_2 = numerical_derivative_1d(square, 2.0)
    return {"slope_at_2": slope_at_2}


if __name__ == "__main__":
    print(run_demo())
