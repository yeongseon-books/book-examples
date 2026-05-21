"""Generated from book-content article."""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=3000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    weights=[0.9, 0.1],
    class_sep=1.0,
    flip_y=0.02,
    random_state=7,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    stratify=y,
    random_state=42,
)

model = LogisticRegression(max_iter=4000).fit(X_train, y_train)
proba = model.predict_proba(X_test)[:, 1]

for threshold in [0.20, 0.35, 0.50, 0.70]:
    pred = (proba >= threshold).astype(int)
    print(
        threshold,
        "precision=", round(precision_score(y_test, pred), 3),
        "recall=", round(recall_score(y_test, pred), 3),
        "flagged=", int(pred.sum()),
        "cm=", confusion_matrix(y_test, pred).tolist(),
    )

print("AP:", round(average_precision_score(y_test, proba), 3))
