from __future__ import annotations

from common import make_synthetic_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def run_demo(seed: int = 42) -> dict[str, float]:
    df = make_synthetic_classification(seed=seed, n=500)
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    model = LogisticRegression(max_iter=1000, random_state=seed)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    return {
        "rows": float(df.shape[0]),
        "accuracy": float(acc),
        "mean_target": float(y.mean()),
    }


if __name__ == "__main__":
    print(run_demo())
