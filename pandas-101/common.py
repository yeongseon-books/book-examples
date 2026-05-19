from __future__ import annotations

import numpy as np
import pandas as pd


def rng(seed: int = 42) -> np.random.Generator:
    return np.random.default_rng(seed)


def make_sales_df(rows: int = 120, seed: int = 42) -> pd.DataFrame:
    gen = rng(seed)
    regions = np.array(["East", "West", "North", "South"])
    channels = np.array(["Online", "Store"])
    categories = np.array(["A", "B", "C"])
    dates = pd.date_range("2024-01-01", periods=rows, freq="D")
    qty = gen.integers(1, 8, size=rows)
    price = gen.uniform(10.0, 80.0, size=rows).round(2)
    discount = gen.choice([0.0, 0.05, 0.1, 0.15], size=rows, p=[0.4, 0.25, 0.2, 0.15])
    df = pd.DataFrame(
        {
            "date": dates,
            "region": gen.choice(regions, size=rows),
            "channel": gen.choice(channels, size=rows),
            "category": gen.choice(categories, size=rows),
            "quantity": qty,
            "price": price,
            "discount": discount,
        }
    )
    df["revenue"] = df["quantity"] * df["price"] * (1 - df["discount"])
    return df


def make_students_df(seed: int = 42) -> pd.DataFrame:
    gen = rng(seed)
    names = ["Kim", "Lee", "Park", "Choi", "Han", "Jung", "Seo", "Lim"]
    scores = gen.integers(55, 100, size=len(names))
    grades = pd.cut(
        scores,
        bins=[0, 69, 79, 89, 100],
        labels=["D", "C", "B", "A"],
        include_lowest=True,
    )
    return pd.DataFrame({"name": names, "score": scores, "grade": grades.astype(str)})
