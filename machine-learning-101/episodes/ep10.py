import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def run() -> dict[str, float]:
    rng = np.random.default_rng(42)
    n = 200
    x_num = rng.normal(size=(n, 3))
    x_cat = rng.choice(["a", "b", "c"], size=(n, 1))
    signal = x_num[:, 0] * 1.2 - x_num[:, 1] * 0.8 + (x_cat[:, 0] == "a").astype(float)
    y = (signal + rng.normal(scale=0.5, size=n) > 0.0).astype(int)
    x = np.hstack([x_num, x_cat])

    xtr, xte, ytr, yte = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=42
    )
    pre = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([("imp", SimpleImputer()), ("sc", StandardScaler())]),
                [0, 1, 2],
            ),
            ("cat", OneHotEncoder(handle_unknown="ignore"), [3]),
        ]
    )
    pipe = Pipeline(
        [("pre", pre), ("clf", LogisticRegression(max_iter=1000, random_state=42))]
    )
    search = GridSearchCV(pipe, {"clf__C": [0.1, 1.0, 10.0]}, cv=3).fit(xtr, ytr)
    return {
        "best_score": float(search.best_score_),
        "test_acc": float(search.score(xte, yte)),
    }
