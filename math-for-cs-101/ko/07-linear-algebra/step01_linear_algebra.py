"""Math For Cs 101 - Episode 1: Linear algebra."""

import numpy as np


def solve_example():
    """Solve example."""
    a = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    return np.linalg.solve(a, b)


def eigenvalues_example():
    """Eigenvalues example."""
    a = np.array([[2.0, 1.0], [1.0, 3.0]])
    return np.linalg.eigvals(a)
