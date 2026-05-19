# English example
import sqlite3

from common import gen_synthetic_sales


def run_demo() -> dict:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE fact_all(order_date TEXT,amount REAL)")
    c.execute("CREATE TABLE fact_2025(order_date TEXT,amount REAL)")
    c.execute("CREATE TABLE fact_2026(order_date TEXT,amount REAL)")
    for d, _, _, amount, _, _ in gen_synthetic_sales(1200, seed=7):
        c.execute("INSERT INTO fact_all VALUES (?,?)", (d, amount))
        c.execute(
            "INSERT INTO fact_2026 VALUES (?,?)"
            if d.startswith("2026")
            else "INSERT INTO fact_2025 VALUES (?,?)",
            (d, amount),
        )
    return {
        "result_rows_all": c.execute(
            "SELECT COUNT(*) FROM fact_all WHERE order_date BETWEEN '2026-01-01' AND '2026-12-31'"
        ).fetchone()[0],
        "result_rows_pruned": c.execute(
            "SELECT COUNT(*) FROM fact_2026 WHERE order_date BETWEEN '2026-01-01' AND '2026-12-31'"
        ).fetchone()[0],
        "scanned_all": c.execute("SELECT COUNT(*) FROM fact_all").fetchone()[0],
        "scanned_pruned": c.execute("SELECT COUNT(*) FROM fact_2026").fetchone()[0],
    }


if __name__ == "__main__":
    print(run_demo())
