from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, fbeta_score, precision_score, recall_score

from common import make_imbalanced, safe_split


def run(seed: int = 42) -> dict[str, float]:
    X, y = make_imbalanced(
        n_samples=1000, weights=(0.87, 0.13), class_sep=0.9, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    pred = model.predict(X_test)
    p = float(precision_score(y_test, pred))
    r = float(recall_score(y_test, pred))
    return {
        "precision": p,
        "recall": r,
        "f1": float(f1_score(y_test, pred)),
        "f2": float(fbeta_score(y_test, pred, beta=2.0)),
        "f05": float(fbeta_score(y_test, pred, beta=0.5)),
    }
