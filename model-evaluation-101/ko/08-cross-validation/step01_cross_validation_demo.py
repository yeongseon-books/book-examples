"""Model Evaluation 101 - 8편: cross validation 예제."""

from __future__ import annotations

import numpy as np
from common import make_imbalanced
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score


def run(seed: int = 42) -> dict[str, float | int]:
    """Run."""
    X, y = make_imbalanced(
        n_samples=900, weights=(0.8, 0.2), class_sep=1.0, random_state=seed
    )
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    model = LogisticRegression(max_iter=1000)
    scores = cross_val_score(model, X, y, cv=cv, scoring="f1")
    return {
        "n_scores": int(len(scores)),
        "mean": float(np.mean(scores)),
        "std": float(np.std(scores)),
    }
