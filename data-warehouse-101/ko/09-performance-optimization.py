"""Data Warehouse 101 - Episode 9: Performance optimization."""

# 한국어 예제
import sqlite3

from common import gen_synthetic_sales


def run_demo() -> dict:
    """Run demo."""
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE fact_sales(order_date TEXT,customer_id TEXT,amount REAL)")
    rows = [
        (d, cid, amount)
        for d, _, cid, amount, _, _ in gen_synthetic_sales(2000, seed=1)
    ]
    c.executemany("INSERT INTO fact_sales VALUES (?,?,?)", rows)
    before = c.execute(
        "EXPLAIN QUERY PLAN SELECT SUM(amount) FROM fact_sales WHERE customer_id='C010'"
    ).fetchall()
    c.execute("CREATE INDEX idx_fact_customer ON fact_sales(customer_id)")
    after = c.execute(
        "EXPLAIN QUERY PLAN SELECT SUM(amount) FROM fact_sales WHERE customer_id='C010'"
    ).fetchall()
    c.execute(
        "CREATE VIEW v_daily AS SELECT order_date,SUM(amount) AS revenue FROM fact_sales GROUP BY order_date"
    )
    return {
        "plan_before": before,
        "plan_after": after,
        "uses_index": any("INDEX" in str(x).upper() for row in after for x in row),
        "preagg_rows": c.execute("SELECT COUNT(*) FROM v_daily").fetchone()[0],
        "col_sum": round(sum(r[2] for r in rows), 2),
        "base_sum": round(
            c.execute("SELECT SUM(amount) FROM fact_sales").fetchone()[0], 2
        ),
    }


if __name__ == "__main__":
    print(run_demo())
