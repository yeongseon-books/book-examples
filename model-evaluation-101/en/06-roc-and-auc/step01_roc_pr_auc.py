"""Model Evaluation 101 - Episode 6: roc and auc example."""

from __future__ import annotations

from common import make_imbalanced, safe_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score


def run(seed: int = 42) -> dict[str, float]:
    """Run."""
    X, y = make_imbalanced(
        n_samples=1000, weights=(0.9, 0.1), class_sep=1.5, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]
    return {
        "auc_roc": float(roc_auc_score(y_test, prob)),
        "auc_pr": float(average_precision_score(y_test, prob)),
    }
