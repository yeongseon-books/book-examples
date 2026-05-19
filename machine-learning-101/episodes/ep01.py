from sklearn.linear_model import LogisticRegression

from common import make_clf_dataset


def run() -> dict[str, float]:
    x, y = make_clf_dataset()
    model = LogisticRegression(max_iter=1000, random_state=42).fit(x, y)
    pred = model.predict(x)
    return {"acc": float((pred == y).mean())}
