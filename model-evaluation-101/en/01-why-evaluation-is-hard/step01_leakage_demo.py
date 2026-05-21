"""Model Evaluation 101 - Episode 1: why evaluation is hard example."""

from __future__ import annotations

from common import make_imbalanced, safe_split
from sklearn.linear_model import LogisticRegression


def run(seed: int = 42) -> dict[str, float]:
    """Run."""
    X, y = make_imbalanced(n_samples=700, class_sep=1.4, random_state=seed)
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    leaked_score = float(model.score(X_train, y_train))
    proper_score = float(model.score(X_test, y_test))
    return {"leaked_train_score": leaked_score, "proper_test_score": proper_score}


if __name__ == "__main__":
    print(run())
