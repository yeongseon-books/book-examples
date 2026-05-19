from __future__ import annotations

from typing import Any, cast

import numpy as np
import pandas as pd
from common import make_synthetic_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split


def interpret_results(seed: int = 42) -> str:
    df = make_synthetic_classification(seed=seed, n=800)
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y
    )
    model = RandomForestClassifier(n_estimators=150, random_state=seed).fit(
        X_train, y_train
    )
    fi = pd.Series(model.feature_importances_, index=X.columns).sort_values(
        ascending=False
    )
    perm = permutation_importance(model, X_test, y_test, n_repeats=8, random_state=seed)
    importances_mean = np.asarray(cast("Any", perm).importances_mean)
    pi = pd.Series(importances_mean, index=X.columns).sort_values(ascending=False)
    top = fi.index[0]
    effect = np.sign(np.corrcoef(X_test[top], model.predict_proba(X_test)[:, 1])[0, 1])
    direction = "increase" if effect >= 0 else "decrease"
    lines = [
        "INTERPRETATION REPORT",
        f"test_accuracy={model.score(X_test, y_test):.3f}",
        "top_feature_importance:",
        fi.head(3).to_string(),
        "top_permutation_importance:",
        pi.head(3).to_string(),
        f"shap_style_note: {top} as the value increases, positive-class probability tends to {direction}.",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(interpret_results())
