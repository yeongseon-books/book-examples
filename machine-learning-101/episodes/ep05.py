from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from common import make_clf_dataset


def run() -> dict[str, float]:
    x, y = make_clf_dataset(class_sep=1.8)
    model = LogisticRegression(max_iter=1000, random_state=42).fit(x, y)
    pred = model.predict(x)
    cm = confusion_matrix(y, pred)
    return {
        "acc": float((pred == y).mean()),
        "tp": float(cm[1, 1]),
        "tn": float(cm[0, 0]),
    }
