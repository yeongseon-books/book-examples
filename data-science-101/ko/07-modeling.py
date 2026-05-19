from __future__ import annotations

from common import make_synthetic_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split


def train_models(seed: int = 42) -> dict[str, float]:
    df = make_synthetic_classification(seed=seed, n=800)
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y
    )

    lr = LogisticRegression(max_iter=1000, random_state=seed).fit(X_train, y_train)
    rf = RandomForestClassifier(n_estimators=120, random_state=seed).fit(
        X_train, y_train
    )
    lr_acc = float(lr.score(X_test, y_test))
    rf_acc = float(rf.score(X_test, y_test))
    cv_mean = float(
        cross_val_score(rf, X_train, y_train, cv=5, scoring="accuracy").mean()
    )
    return {"logreg_accuracy": lr_acc, "rf_accuracy": rf_acc, "rf_cv_accuracy": cv_mean}


if __name__ == "__main__":
    print(train_models())
