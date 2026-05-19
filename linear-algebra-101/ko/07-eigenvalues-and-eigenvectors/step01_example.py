"""Linear Algebra 101 - Episode 1: Example."""

import numpy as np
from common import power_iteration


def run():
    """Run."""
    np.random.seed(0)
    a = np.array([[4.0, 1.0], [2.0, 3.0]])
    vals, vecs = np.linalg.eig(a)
    lmax, vmax = power_iteration(a, seed=0)
    print("eigenvalues:", vals)
    print("dominant eigenvalue:", lmax)
    return {"a": a, "vals": vals, "vecs": vecs, "lmax": lmax, "vmax": vmax}


if __name__ == "__main__":
    run()
