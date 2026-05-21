"""Calculus For Ml 101 - Episode 6: loss function example."""

import math


def mse(y: list[float], p: list[float]) -> float:
    """Mse."""
    return sum((yi - pi) ** 2 for yi, pi in zip(y, p, strict=False)) / len(y)


def mse_grad(y: list[float], p: list[float]) -> list[float]:
    """Mse grad."""
    n = len(y)
    return [-2 * (yi - pi) / n for yi, pi in zip(y, p, strict=False)]


def bce(y: list[float], p: list[float], eps: float = 1e-7) -> float:
    """Bce."""
    return -sum(
        yi * math.log(pi + eps) + (1 - yi) * math.log(1 - pi + eps)
        for yi, pi in zip(y, p, strict=False)
    ) / len(y)


def run_demo() -> dict[str, float | list[float]]:
    """Run demo."""
    y = [1.0, 0.0, 1.0]
    p = [0.9, 0.2, 0.7]
    return {"mse": mse(y, p), "mse_grad": mse_grad(y, p), "bce": bce(y, p)}
