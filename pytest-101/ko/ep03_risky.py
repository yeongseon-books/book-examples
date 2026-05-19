"""Pytest 101 - Episode 3: Risky."""

import warnings


def divide_positive(numerator: float, denominator: float) -> float:
    """Divide positive."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    if numerator < 0 or denominator < 0:
        warnings.warn("negative input may be unexpected", UserWarning, stacklevel=2)
    return numerator / denominator
