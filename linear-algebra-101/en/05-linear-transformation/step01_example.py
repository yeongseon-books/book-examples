"""Linear Algebra 101 - Episode 5: linear transformation example."""

import numpy as np


def run():
    """Run."""
    np.random.seed(0)
    theta = np.pi / 4
    r = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    s = np.diag([1.5, 0.5])
    sh = np.array([[1.0, 0.7], [0.0, 1.0]])
    pts = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [-1.0, 1.0]])
    transformed = (sh @ s @ r @ pts.T).T
    print("first point:", transformed[0])
    return {
        "rotation": r,
        "scale": s,
        "shear": sh,
        "points": pts,
        "transformed": transformed,
    }


if __name__ == "__main__":
    run()
