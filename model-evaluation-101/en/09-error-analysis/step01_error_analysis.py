from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from common import make_imbalanced, print_confusion, safe_split


def run(seed: int = 42) -> dict[str, object]:
    X, y = make_imbalanced(
        n_samples=1000, weights=(0.8, 0.2), class_sep=1.0, random_state=seed
    )
    X_train, _, X_test, y_train, _, y_test = safe_split(X, y, random_state=seed)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]
    pred = (prob >= 0.5).astype(int)
    mask = pred != y_test
    mis_idx = np.where(mask)[0][:5].tolist()
    report = classification_report(y_test, pred, output_dict=True)
    return {
        "confusion": print_confusion(y_test, pred),
        "class_0_precision": float(report["0"]["precision"]),
        "class_1_recall": float(report["1"]["recall"]),
        "misclassified_examples": mis_idx,
    }
