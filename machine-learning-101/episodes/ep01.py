"""Machine Learning 101 - Episode 1."""

from common import make_clf_dataset
from sklearn.linear_model import LogisticRegression


def run() -> dict[str, float]:
    """Run."""
    x, y = make_clf_dataset()
    model = LogisticRegression(max_iter=1000, random_state=42).fit(x, y)
    pred = model.predict(x)
    return {"acc": float((pred == y).mean())}
