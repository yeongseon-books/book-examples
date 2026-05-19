from __future__ import annotations

import pandas as pd
from common import make_dirty_dataset


def clean_dataset(seed: int = 42) -> pd.DataFrame:
    df = make_dirty_dataset(seed=seed, n=300).copy()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.drop_duplicates(subset=["user_id"], keep="last")
    df["country"] = df["country"].fillna("UNKNOWN")
    df["age"] = df["age"].fillna(df["age"].median())
    df["amount"] = df["amount"].fillna(df["amount"].median())
    q1, q3 = df["amount"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["amount"] = df["amount"].clip(lower=lower, upper=upper)
    return df.reset_index(drop=True)


if __name__ == "__main__":
    cleaned = clean_dataset()
    print({"rows": cleaned.shape[0], "nulls": int(cleaned.isna().sum().sum())})
