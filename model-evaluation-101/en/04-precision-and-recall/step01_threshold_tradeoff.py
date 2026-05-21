"""Model Evaluation 101 - Episode 4: precision and recall example."""

from __future__ import annotations

from common import compute_pr_at_threshold, make_imbalanced, safe_split
from sklearn.linear_model import LogisticRegression


def run(seed: int = 42) -> dict[str, dict[str, float]]:
    """Run."""
    X, y = make_imbalanced(
        n_samples=1000, weights=(0.9, 0.1), class_sep=1.0, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]
    return {
        "t03": compute_pr_at_threshold(y_test, prob, 0.3),
        "t05": compute_pr_at_threshold(y_test, prob, 0.5),
        "t07": compute_pr_at_threshold(y_test, prob, 0.7),
    }
