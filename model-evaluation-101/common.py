"""Shared utilities and domain models for Model Evaluation 101."""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import (
    accuracy_score,
    brier_score_loss,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


def make_imbalanced(
    n_samples: int = 600,
    weights: tuple[float, float] = (0.9, 0.1),
    class_sep: float = 1.0,
    random_state: int = 42,
) -> tuple[Any, Any]:
    """Make imbalanced."""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=8,
        n_informative=4,
        n_redundant=0,
        n_clusters_per_class=1,
        weights=list(weights),
        class_sep=class_sep,
        random_state=random_state,
    )
    return X, y


def safe_split(
    X: np.ndarray,
    y: np.ndarray,
    random_state: int = 42,
) -> tuple[Any, Any, Any, Any, Any, Any]:
    """Safe split."""
    X_train, X_rest, y_train, y_rest = train_test_split(
        X,
        y,
        test_size=0.4,
        stratify=y,
        random_state=random_state,
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_rest,
        y_rest,
        test_size=0.5,
        stratify=y_rest,
        random_state=random_state,
    )
    return X_train, X_val, X_test, y_train, y_val, y_test


def compute_pr_at_threshold(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float,
) -> dict[str, float]:
    """Compute pr at threshold."""
    y_pred = (y_prob >= threshold).astype(int)
    return {
        "precision": float(precision_score(y_true, y_pred)),
        "recall": float(recall_score(y_true, y_pred)),
    }


def print_confusion(y_true: np.ndarray, y_pred: np.ndarray) -> str:
    """Print confusion."""
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    return f"TN={tn} FP={fp} FN={fn} TP={tp}"


def evaluation_report(
    model: Any,
    X: np.ndarray,
    y: np.ndarray,
    threshold: float = 0.5,
) -> dict[str, Any]:
    """Evaluation report."""
    prob = model.predict_proba(X)[:, 1]
    pred = (prob >= threshold).astype(int)
    cm = confusion_matrix(y, pred)
    report: dict[str, Any] = {
        "threshold": float(threshold),
        "n_samples": int(len(y)),
        "positive_rate": float(np.mean(y)),
        "accuracy": float(accuracy_score(y, pred)),
        "precision": float(precision_score(y, pred)),
        "recall": float(recall_score(y, pred)),
        "f1": float(f1_score(y, pred)),
        "auc_roc": float(roc_auc_score(y, prob)),
        "brier": float(brier_score_loss(y, prob)),
        "confusion_matrix": cm.astype(int).tolist(),
    }
    return report
