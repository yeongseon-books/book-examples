"""Generated from book-content article."""

from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    recall_score,
)
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=5000,
    n_features=20,
    n_informative=5,
    n_redundant=2,
    weights=[0.96, 0.04],
    class_sep=1.1,
    flip_y=0.015,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42,
)

dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
model = LogisticRegression(max_iter=4000).fit(X_train, y_train)
pred = model.predict(X_test)

print("base rate:", round(y.mean(), 4))
print("dummy accuracy:", round(dummy.score(X_test, y_test), 4))
print("model accuracy:", round(accuracy_score(y_test, pred), 4))
print("minority recall:", round(recall_score(y_test, pred), 4))
print("balanced accuracy:", round(balanced_accuracy_score(y_test, pred), 4))
print("confusion matrix:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, digits=4))
