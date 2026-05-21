"""Generated from book-content article."""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=5000,
    n_features=12,
    n_informative=5,
    n_redundant=3,
    weights=[0.96, 0.04],
    class_sep=1.2,
    flip_y=0.02,
    random_state=31,
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

fpr, tpr, thresholds = roc_curve(y_test, proba)
print("ROC-AUC:", round(roc_auc_score(y_test, proba), 3))
print("PR-AUC:", round(average_precision_score(y_test, proba), 3))

target_fpr = 0.05
idx = max(i for i, value in enumerate(fpr) if value <= target_fpr)
threshold = thresholds[idx]
pred = (proba >= threshold).astype(int)

cm = confusion_matrix(y_test, pred)
tn, fp, fn, tp = cm.ravel()
precision = precision_score(y_test, pred, zero_division=0)
recall = recall_score(y_test, pred, zero_division=0)
decision_cost = fp * 1 + fn * 10

print("chosen threshold:", round(float(threshold), 3))
print("FPR:", round(fp / (fp + tn), 3))
print("precision:", round(precision, 3))
print("recall:", round(recall, 3))
print("confusion matrix:", cm.tolist())
print("cost (FP=1, FN=10):", decision_cost)
