from __future__ import annotations

from common import make_imbalanced, safe_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score


def run(seed: int = 42) -> dict[str, float]:
    X, y = make_imbalanced(
        n_samples=1200, weights=(0.95, 0.05), class_sep=0.8, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    pred_dummy = dummy.predict(X_test)
    base_acc = float(accuracy_score(y_test, pred_dummy))
    base_rec = float(recall_score(y_test, pred_dummy))
    model = LogisticRegression(max_iter=1000, class_weight="balanced").fit(
        X_train, y_train
    )
    pred_bal = model.predict(X_test)
    bal_acc = float(accuracy_score(y_test, pred_bal))
    bal_rec = float(recall_score(y_test, pred_bal))
    return {
        "dummy_accuracy": base_acc,
        "dummy_recall": base_rec,
        "balanced_accuracy": bal_acc,
        "balanced_recall": bal_rec,
    }
