"""Linear Algebra 101 - Episode 1: Example."""

import numpy as np


def run():
    """Run."""
    np.random.seed(0)
    v = np.array([3.0, 4.0])
    w = np.array([1.0, -2.0])
    added = v + w
    scaled = 2.0 * v
    dot = float(v @ w)
    norm = float(np.linalg.norm(v))
    unit = v / norm
    print("dot:", dot)
    print("norm:", norm)
    print("unit norm:", np.linalg.norm(unit))
    return {"added": added, "scaled": scaled, "dot": dot, "norm": norm, "unit": unit}


if __name__ == "__main__":
    run()
