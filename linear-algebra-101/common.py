"""Shared utilities and domain models for Linear Algebra 101."""

import numpy as np


def make_random_matrix(seed: int, rows: int = 3, cols: int = 3) -> np.ndarray:
    """Make random matrix."""
    rng = np.random.default_rng(seed)
    return rng.normal(size=(rows, cols))


def gram_schmidt(vectors: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Gram schmidt."""
    basis = []
    for v in vectors:
        w = v.astype(float).copy()
        for b in basis:
            w -= np.dot(w, b) * b
        n = np.linalg.norm(w)
        if n > tol:
            basis.append(w / n)
    if not basis:
        return np.empty((0, vectors.shape[1]))
    return np.vstack(basis)


def power_iteration(
    a: np.ndarray, num_iter: int = 200, seed: int = 0
) -> tuple[float, np.ndarray]:
    """Power iteration."""
    rng = np.random.default_rng(seed)
    b_k = rng.normal(size=(a.shape[1],))
    b_k = b_k / np.linalg.norm(b_k)
    for _ in range(num_iter):
        b_k1 = a @ b_k
        n = np.linalg.norm(b_k1)
        if n == 0:
            break
        b_k = b_k1 / n
    eigenvalue = float(b_k.T @ a @ b_k)
    return eigenvalue, b_k


def pca_fit(
    x: np.ndarray, n_components: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Pca fit."""
    x_centered = x - x.mean(axis=0)
    _, s, vt = np.linalg.svd(x_centered, full_matrices=False)
    components = vt[:n_components]
    transformed = x_centered @ components.T
    var_ratio = (s**2) / np.sum(s**2)
    return components, transformed, var_ratio, x_centered


def text_histogram(values: np.ndarray, bins: int = 8, width: int = 24) -> list[str]:
    """Text histogram."""
    hist, edges = np.histogram(values, bins=bins)
    max_count = int(hist.max()) if hist.size else 1
    lines = []
    for i, c in enumerate(hist):
        bar_len = int(width * (c / max_count)) if max_count else 0
        lines.append(f"[{edges[i]:6.2f}, {edges[i + 1]:6.2f}) | " + ("#" * bar_len))
    return lines


def fit_linear_regression_normal_eq(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Fit linear regression normal eq."""
    return np.linalg.solve(x.T @ x, x.T @ y)


def fit_logistic_regression_gd(
    x: np.ndarray,
    y: np.ndarray,
    lr: float = 0.5,
    steps: int = 2000,
    seed: int = 0,
) -> np.ndarray:
    """Fit logistic regression gd."""
    rng = np.random.default_rng(seed)
    w = rng.normal(scale=0.01, size=x.shape[1])
    for _ in range(steps):
        z = x @ w
        p = 1.0 / (1.0 + np.exp(-z))
        grad = x.T @ (p - y) / len(y)
        w -= lr * grad
    return w
