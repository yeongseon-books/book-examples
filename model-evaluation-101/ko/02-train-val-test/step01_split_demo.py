"""Model Evaluation 101 - 2편: train val test 예제."""

from __future__ import annotations

import numpy as np
from common import make_imbalanced, safe_split


def run(seed: int = 42) -> dict[str, float]:
    """Run."""
    X, y = make_imbalanced(n_samples=600, weights=(0.85, 0.15), random_state=seed)
    X_train, X_val, X_test, y_train, y_val, y_test = safe_split(X, y, random_state=seed)
    train_ratio = len(X_train) / len(X)
    val_ratio = len(X_val) / len(X)
    test_ratio = len(X_test) / len(X)
    return {
        "train_ratio": train_ratio,
        "val_ratio": val_ratio,
        "test_ratio": test_ratio,
        "full_pos_rate": float(np.mean(y)),
        "train_pos_rate": float(np.mean(y_train)),
        "val_pos_rate": float(np.mean(y_val)),
        "test_pos_rate": float(np.mean(y_test)),
    }


if __name__ == "__main__":
    print(run())
