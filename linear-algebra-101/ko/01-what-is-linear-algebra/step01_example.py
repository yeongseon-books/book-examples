"""Linear Algebra 101 - 1편: what is linear algebra 예제."""

import numpy as np


def run():
    """Run."""
    np.random.seed(0)
    v = np.array([3.0, 4.0])
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    y = a @ v
    print("vector shape:", v.shape)
    print("matrix shape:", a.shape)
    print("Av:", y)
    return {"v_shape": v.shape, "a_shape": a.shape, "y": y}


if __name__ == "__main__":
    run()
