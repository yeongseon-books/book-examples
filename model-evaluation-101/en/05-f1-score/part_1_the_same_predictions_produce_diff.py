"""Generated from book-content article."""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, fbeta_score
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=3200,
    n_features=12,
    n_informative=6,
    n_redundant=2,
    n_classes=3,
    n_clusters_per_class=1,
    weights=[0.65, 0.25, 0.10],
    class_sep=1.1,
    flip_y=0.02,
    random_state=11,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42,
)

model = LogisticRegression(max_iter=4000).fit(X_train, y_train)
pred = model.predict(X_test)

print("micro:", round(f1_score(y_test, pred, average="micro"), 3))
print("macro:", round(f1_score(y_test, pred, average="macro"), 3))
print("weighted:", round(f1_score(y_test, pred, average="weighted"), 3))
print("per class:", [round(x, 3) for x in f1_score(y_test, pred, average=None)])
print("F2 macro:", round(fbeta_score(y_test, pred, beta=2, average="macro"), 3))
print("F0.5 macro:", round(fbeta_score(y_test, pred, beta=0.5, average="macro"), 3))
