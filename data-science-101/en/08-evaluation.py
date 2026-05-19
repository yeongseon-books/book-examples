"""Data Science 101 - Episode 8: Evaluation."""

from __future__ import annotations

import math

import numpy as np
from common import make_synthetic_classification, make_synthetic_regression
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


def manual_classification_metrics(
    y_true: np.ndarray, y_pred: np.ndarray
) -> dict[str, float]:
    """Manual classification metrics."""
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    )
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}


def manual_regression_metrics(
    y_true: np.ndarray, y_pred: np.ndarray
) -> dict[str, float]:
    """Manual regression metrics."""
    errors = y_true - y_pred
    mae = float(np.abs(errors).mean())
    rmse = float(math.sqrt((errors**2).mean()))
    sst = float(((y_true - y_true.mean()) ** 2).sum())
    ssr = float(((y_true - y_pred) ** 2).sum())
    r2 = 1.0 - ssr / sst
    return {"mae": mae, "rmse": rmse, "r2": r2}


def compare_metrics(seed: int = 42) -> dict[str, float]:
    """Compare metrics."""
    cdf = make_synthetic_classification(seed=seed, n=700)
    Xc, yc = cdf.drop(columns=["target"]), cdf["target"]
    Xtr, Xte, ytr, yte = train_test_split(
        Xc, yc, test_size=0.2, random_state=seed, stratify=yc
    )
    clf = LogisticRegression(max_iter=1000, random_state=seed).fit(Xtr, ytr)
    pred = clf.predict(Xte)
    proba = clf.predict_proba(Xte)[:, 1]

    m_cls = manual_classification_metrics(yte.to_numpy(), pred)
    s_cls = {
        "accuracy": accuracy_score(yte, pred),
        "precision": precision_score(yte, pred),
        "recall": recall_score(yte, pred),
        "f1": f1_score(yte, pred),
        "roc_auc": roc_auc_score(yte, proba),
    }

    rdf = make_synthetic_regression(seed=seed, n=700)
    Xr, yr = rdf.drop(columns=["target"]), rdf["target"]
    Xtr, Xte, ytr, yte = train_test_split(Xr, yr, test_size=0.2, random_state=seed)
    reg = LinearRegression().fit(Xtr, ytr)
    ypred = reg.predict(Xte)

    m_reg = manual_regression_metrics(yte.to_numpy(), ypred)
    s_reg = {
        "mae": mean_absolute_error(yte, ypred),
        "rmse": math.sqrt(mean_squared_error(yte, ypred)),
        "r2": r2_score(yte, ypred),
    }

    return {
        "manual_f1": m_cls["f1"],
        "sklearn_f1": float(s_cls["f1"]),
        "manual_rmse": m_reg["rmse"],
        "sklearn_rmse": float(s_reg["rmse"]),
        "roc_auc": float(s_cls["roc_auc"]),
    }


if __name__ == "__main__":
    print(compare_metrics())
