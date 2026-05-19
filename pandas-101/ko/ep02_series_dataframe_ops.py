"""Pandas 101 - Episode 2: Series dataframe ops."""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
from common import make_sales_df, make_students_df


def run() -> dict[str, object]:
    # EP01
    """Run."""
    pd.Series([10, 20, 30], name="sales")
    df1 = pd.DataFrame(
        {
            "product": ["A", "B", "C", "D"],
            "qty": [3, 5, 2, 7],
            "price": [12.0, 8.0, 15.0, 5.0],
        }
    )
    dtypes = df1.dtypes.astype(str).to_dict()
    shape = df1.shape
    describe_mean = float(df1[["qty", "price"]].describe().loc["mean", "qty"])

    # EP02
    indexed = make_students_df(seed=7)
    row_loc = indexed.loc[0, "name"]
    row_iloc = int(indexed.iloc[1]["score"])
    high = indexed[indexed["score"] >= 80]

    # EP03
    csv_df = pd.DataFrame(
        {"id": [1, 2, 3], "name": ["alpha", "beta", "gamma"], "value": [2.5, 3.0, 4.5]}
    )
    with tempfile.TemporaryDirectory() as tmp:
        csv_path = Path(tmp) / "sample.csv"
        xlsx_path = Path(tmp) / "sample.xlsx"
        csv_df.to_csv(csv_path, index=False)
        csv_df.to_excel(xlsx_path, index=False)
        loaded_csv = pd.read_csv(csv_path)
        loaded_xlsx = pd.read_excel(xlsx_path)

    # EP04
    sales = make_sales_df(rows=40, seed=11)
    filt = sales[(sales["region"] == "East") & (sales["quantity"].between(2, 5))]
    queried = sales.query("channel == 'Online' and discount >= 0.1")
    isin_rows = sales[sales["category"].isin(["A", "C"])]

    # EP05
    na_df = pd.DataFrame(
        {"a": [1.0, np.nan, 3.0, np.nan], "b": [np.nan, 2.0, np.nan, 4.0]}
    )
    na_count = int(na_df.isna().sum().sum())
    fill_mean = na_df.fillna(na_df.mean(numeric_only=True))
    fill_ffill = na_df.ffill()
    dropped = na_df.dropna()
    interpolated = na_df.interpolate(limit_direction="both")

    # EP06
    grouped = sales.groupby(["region", "channel"]).agg(
        total_qty=("quantity", "sum"),
        avg_price=("price", "mean"),
        total_revenue=("revenue", "sum"),
    )
    sales["region_revenue_share"] = sales["revenue"] / sales.groupby("region")[
        "revenue"
    ].transform("sum")

    # EP07
    left = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
    right = pd.DataFrame({"id": [2, 3, 4], "score": [85, 90, 88]})
    inner = left.merge(right, on="id", how="inner")
    outer = left.merge(right, on="id", how="outer")
    joined = left.set_index("id").join(right.set_index("id"), how="left")
    concat = pd.concat([left.assign(src="L"), left.assign(src="L2")], ignore_index=True)

    # EP08
    ts = sales.set_index("date").sort_index()[["revenue", "quantity"]]
    daily = ts.resample("D").sum()
    weekly = ts.resample("W").sum()
    monthly = ts.resample("M").sum()
    rolling_7d = daily["revenue"].rolling(7, min_periods=1).mean()

    # EP09
    cost_df = sales[["quantity", "price", "discount"]].copy()
    applied = cost_df.apply(
        lambda r: r["quantity"] * r["price"] * (1 - r["discount"]), axis=1
    )
    vectorized = cost_df["quantity"] * cost_df["price"] * (1 - cost_df["discount"])
    max_diff = float((applied - vectorized).abs().max())

    # EP10
    end = make_sales_df(rows=120, seed=100)
    end.loc[end.index[::19], "price"] = np.nan
    end["price"] = end["price"].fillna(
        end.groupby("category")["price"].transform("mean")
    )
    end["net_revenue"] = end["quantity"] * end["price"] * (1 - end["discount"])
    insights = (
        end.groupby(["region", "category"], as_index=False)
        .agg(
            total_revenue=("net_revenue", "sum"),
            avg_discount=("discount", "mean"),
            orders=("quantity", "count"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    return {
        "ep01": {"shape": shape, "dtypes": dtypes, "describe_mean_qty": describe_mean},
        "ep02": {
            "loc_name": row_loc,
            "iloc_score": row_iloc,
            "high_count": int(high.shape[0]),
        },
        "ep03": {
            "csv_shape": loaded_csv.shape,
            "excel_shape": loaded_xlsx.shape,
            "columns": list(loaded_csv.columns),
        },
        "ep04": {
            "filter_count": int(filt.shape[0]),
            "query_count": int(queried.shape[0]),
            "isin_count": int(isin_rows.shape[0]),
        },
        "ep05": {
            "na_count": na_count,
            "mean_fill_nulls": int(fill_mean.isna().sum().sum()),
            "ffill_nulls": int(fill_ffill.isna().sum().sum()),
            "dropna_rows": int(dropped.shape[0]),
            "interpolate_nulls": int(interpolated.isna().sum().sum()),
        },
        "ep06": {
            "group_shape": grouped.shape,
            "share_sum": float(
                sales.groupby("region")["region_revenue_share"].sum().mean()
            ),
        },
        "ep07": {
            "inner_shape": inner.shape,
            "outer_shape": outer.shape,
            "join_shape": joined.shape,
            "concat_shape": concat.shape,
        },
        "ep08": {
            "daily_rows": int(daily.shape[0]),
            "weekly_rows": int(weekly.shape[0]),
            "monthly_rows": int(monthly.shape[0]),
            "rolling_last": float(rolling_7d.iloc[-1]),
        },
        "ep09": {
            "max_diff": max_diff,
            "same_values": bool(np.allclose(applied.to_numpy(), vectorized.to_numpy())),
        },
        "ep10": {
            "insights_rows": int(insights.shape[0]),
            "top_region": str(insights.iloc[0]["region"]),
            "total_revenue": float(end["net_revenue"].sum()),
        },
    }


if __name__ == "__main__":
    out = run()
    for ep, result in out.items():
        print(ep, result)
