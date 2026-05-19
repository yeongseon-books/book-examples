"""Data Science 101 - Episode 5: Exploratory data analysis."""

from __future__ import annotations

import pandas as pd
from common import make_synthetic_classification


def make_eda_report(seed: int = 42) -> str:
    """Make eda report."""
    df = make_synthetic_classification(seed=seed, n=600)
    feature_cols = [c for c in df.columns if c.startswith("feature_")]
    desc = df[feature_cols].describe().round(3)
    corr = df[feature_cols + ["target"]].corr().round(3)
    bins = pd.cut(df["feature_0"], bins=4)
    grouped = df.groupby(bins, observed=False)["target"].mean().round(3)
    lines = [
        "EDA REPORT",
        f"rows={df.shape[0]}, cols={df.shape[1]}",
        "descriptive_stats:",
        desc.to_string(),
        "correlation_matrix:",
        corr.to_string(),
        "target_by_feature0_bucket:",
        grouped.to_string(),
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(make_eda_report())
