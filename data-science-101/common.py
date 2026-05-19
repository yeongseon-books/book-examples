from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression


def make_synthetic_classification(seed: int = 42, n: int = 500) -> pd.DataFrame:
    X, y = make_classification(
        n_samples=n,
        n_features=6,
        n_informative=4,
        n_redundant=1,
        class_sep=1.2,
        random_state=seed,
    )
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
    df["target"] = y
    return df


def make_synthetic_regression(seed: int = 42, n: int = 500) -> pd.DataFrame:
    X, y = make_regression(
        n_samples=n,
        n_features=5,
        n_informative=4,
        noise=12.0,
        random_state=seed,
    )
    df = pd.DataFrame(X, columns=[f"reg_feature_{i}" for i in range(X.shape[1])])
    df["target"] = y
    return df


def make_dirty_dataset(seed: int = 42, n: int = 300) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = pd.DataFrame(
        {
            "user_id": [f"U{i:04d}" for i in range(n)],
            "age": rng.integers(18, 70, size=n).astype(float),
            "country": rng.choice(
                ["KR", "US", "JP", None], size=n, p=[0.4, 0.3, 0.2, 0.1]
            ),
            "amount": rng.normal(120.0, 35.0, size=n),
        }
    )
    df.loc[rng.choice(n, size=20, replace=False), "age"] = np.nan
    df.loc[rng.choice(n, size=15, replace=False), "amount"] = np.nan
    df.loc[:10, "amount"] = 10000.0
    dirty = pd.concat([df, df.iloc[:15]], ignore_index=True)
    dirty["age"] = dirty["age"].astype("string")
    return dirty


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def summarize_dataframe(df: pd.DataFrame) -> dict[str, Any]:
    return {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": list(df.columns),
        "nulls": {k: int(v) for k, v in df.isna().sum().to_dict().items()},
    }
