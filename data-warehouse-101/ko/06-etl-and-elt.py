# 한국어 예제
import sqlite3

import pandas as pd


def run_demo() -> dict:
    src = pd.DataFrame(
        [
            {"order_id": 1, "region": "KR", "amount": 10.0},
            {"order_id": 2, "region": "US", "amount": 20.0},
            {"order_id": 3, "region": "KR", "amount": 15.0},
        ]
    )
    etl = src.groupby("region", as_index=False)["amount"].sum().sort_values("region")
    conn = sqlite3.connect(":memory:")
    src.to_sql("raw_orders", conn, index=False)
    elt = pd.read_sql_query(
        "SELECT region,SUM(amount) AS amount FROM raw_orders GROUP BY region ORDER BY region",
        conn,
    )
    return {
        "etl": list(map(tuple, etl.values.tolist())),
        "elt": list(map(tuple, elt.values.tolist())),
    }


if __name__ == "__main__":
    print(run_demo())
