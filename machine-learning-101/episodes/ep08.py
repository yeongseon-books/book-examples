"""Machine Learning 101 - Episode 8."""

import numpy as np
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split


def run() -> dict[str, float]:
    """Run."""
    rng = np.random.default_rng(42)
    x1 = rng.normal(size=200)
    x2 = x1 + rng.normal(scale=0.05, size=200)
    x3 = rng.normal(size=200)
    x = np.column_stack([x1, x2, x3])
    y = 4.0 * x1 - 3.0 * x3 + rng.normal(scale=1.0, size=200)
    xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.3, random_state=42)

    ols = LinearRegression().fit(xtr, ytr)
    ridge = Ridge(alpha=10.0).fit(xtr, ytr)
    lasso = Lasso(alpha=0.1, max_iter=5000).fit(xtr, ytr)
    return {
        "ols_gap": float(ols.score(xtr, ytr) - ols.score(xte, yte)),
        "ridge_norm": float(np.linalg.norm(ridge.coef_)),
        "ols_norm": float(np.linalg.norm(ols.coef_)),
        "lasso_zero": float((np.abs(lasso.coef_) < 1e-8).sum()),
    }
