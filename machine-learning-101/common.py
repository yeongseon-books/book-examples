"""Shared utilities and domain models for Machine Learning 101."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.datasets import make_classification, make_regression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

SEED = 42


@dataclass
class ScoreResult:
    """Score result."""

    primary: float
    secondary: float


def make_clf_dataset(
    n_samples: int = 200, *, class_sep: float = 1.5
) -> tuple[np.ndarray, np.ndarray]:
    """Make clf dataset."""
    x, y = make_classification(
        n_samples=n_samples,
        n_features=6,
        n_informative=4,
        n_redundant=0,
        n_classes=2,
        class_sep=class_sep,
        random_state=SEED,
    )
    return x, y


def make_reg_dataset(n_samples: int = 200) -> tuple[np.ndarray, np.ndarray]:
    """Make reg dataset."""
    x, y = make_regression(
        n_samples=n_samples,
        n_features=6,
        n_informative=4,
        noise=5.0,
        random_state=SEED,
    )
    return x, y


def score_model(kind: str, y_true: np.ndarray, y_pred: np.ndarray) -> ScoreResult:
    """Score model."""
    if kind == "clf":
        return ScoreResult(primary=float(accuracy_score(y_true, y_pred)), secondary=0.0)
    mse = float(mean_squared_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return ScoreResult(primary=r2, secondary=mse)


def print_report(title: str, metrics: dict[str, float]) -> None:
    """Print report."""
    print(f"== {title} ==")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")
