"""Linear Algebra 101 - 6편: basis and dimension 예제."""

import numpy as np
from common import gram_schmidt


def run():
    """Run."""
    np.random.seed(0)
    a = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 2.0]])
    rank = int(np.linalg.matrix_rank(a))
    basis = gram_schmidt(a.T)
    print("rank:", rank)
    print("basis vectors:", basis.shape[0])
    return {"a": a, "rank": rank, "basis": basis}


if __name__ == "__main__":
    run()
