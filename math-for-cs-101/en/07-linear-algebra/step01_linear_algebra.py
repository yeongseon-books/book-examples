import numpy as np


def solve_example():
    a = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    return np.linalg.solve(a, b)


def eigenvalues_example():
    a = np.array([[2.0, 1.0], [1.0, 3.0]])
    return np.linalg.eigvals(a)
