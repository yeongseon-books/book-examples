"""Linear Algebra 101 - Episode 3: matrices example."""

import numpy as np


def run():
    """Run."""
    np.random.seed(0)
    a = np.array([[2.0, 1.0], [5.0, 3.0]])
    b = np.array([[1.0, 4.0], [2.0, 0.0]])
    at = a.T
    ab = a @ b
    inv = np.linalg.inv(a)
    det = float(np.linalg.det(a))
    print("det(A):", det)
    print("A @ inv(A):", a @ inv)
    return {"a": a, "at": at, "ab": ab, "inv": inv, "det": det}


if __name__ == "__main__":
    run()
