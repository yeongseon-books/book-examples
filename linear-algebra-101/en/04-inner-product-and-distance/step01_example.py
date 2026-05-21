"""Linear Algebra 101 - Episode 4: inner product and distance example."""

import numpy as np


def run():
    """Run."""
    np.random.seed(0)
    docs = np.array([[2.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 2.0]])
    q = np.array([1.0, 1.0, 0.0])
    dot = docs @ q
    norms = np.linalg.norm(docs, axis=1) * np.linalg.norm(q)
    cosine = dot / norms
    euclidean = np.linalg.norm(docs - q, axis=1)
    manhattan = np.sum(np.abs(docs - q), axis=1)
    print("cosine:", cosine)
    print("euclidean:", euclidean)
    return {"cosine": cosine, "euclidean": euclidean, "manhattan": manhattan}


if __name__ == "__main__":
    run()
