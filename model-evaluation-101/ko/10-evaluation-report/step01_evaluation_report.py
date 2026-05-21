"""Model Evaluation 101 - 10편: evaluation report 예제."""

from __future__ import annotations

from common import evaluation_report, make_imbalanced, safe_split
from sklearn.linear_model import LogisticRegression


def run(seed: int = 42) -> dict[str, object]:
    """Run."""
    X, y = make_imbalanced(
        n_samples=1000, weights=(0.82, 0.18), class_sep=1.2, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    return evaluation_report(model, X_test, y_test, threshold=0.5)
