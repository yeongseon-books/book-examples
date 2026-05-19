import numpy as np


def loss(w: np.ndarray) -> float:
    return float((w[0] - 1) ** 2 + (w[1] + 2) ** 2)


def gradient(w: np.ndarray) -> np.ndarray:
    return np.array([2 * (w[0] - 1), 2 * (w[1] + 2)], dtype=float)


def step(w: np.ndarray, lr: float = 0.1) -> np.ndarray:
    return w - lr * gradient(w)


def run_demo() -> dict[str, np.ndarray | float]:
    w0 = np.array([0.0, 0.0])
    g = gradient(w0)
    return {"grad": g, "norm": float(np.linalg.norm(g)), "next_loss": loss(step(w0))}
