"""Generated from book-content article."""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=4000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    weights=[0.88, 0.12],
    class_sep=1.0,
    flip_y=0.02,
    random_state=19,
)

X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.4,
    stratify=y,
    random_state=42,
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    stratify=y_temp,
    random_state=42,
)

model = LogisticRegression(max_iter=4000).fit(X_train, y_train)
val_proba = model.predict_proba(X_val)[:, 1]
test_proba = model.predict_proba(X_test)[:, 1]

thresholds = np.arange(0.10, 0.91, 0.05)
rows = []
for threshold in thresholds:
    val_pred = (val_proba >= threshold).astype(int)
    rows.append(
        (
            round(float(threshold), 2),
            f1_score(y_val, val_pred),
            precision_score(y_val, val_pred, zero_division=0),
            recall_score(y_val, val_pred, zero_division=0),
        )
    )

best_threshold, best_val_f1, _, _ = max(rows, key=lambda row: row[1])
print("validation sweep:")
for threshold, f1, precision, recall in rows:
    if threshold in {0.20, 0.30, 0.50, 0.70}:
        print(threshold, round(f1, 3), round(precision, 3), round(recall, 3))

print("best validation threshold:", best_threshold, round(best_val_f1, 3))

locked_test_pred = (test_proba >= best_threshold).astype(int)
print(
    "locked test:",
    round(f1_score(y_test, locked_test_pred), 3),
    round(precision_score(y_test, locked_test_pred), 3),
    round(recall_score(y_test, locked_test_pred), 3),
)

business_pred = (test_proba >= 0.50).astype(int)
print(
    "business threshold 0.50:",
    round(f1_score(y_test, business_pred), 3),
    round(precision_score(y_test, business_pred), 3),
    round(recall_score(y_test, business_pred), 3),
)
