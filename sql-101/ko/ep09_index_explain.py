"""Sql 101 - Episode 9: Index explain."""

from common import seed_db


def run_demo():
    """Run demo."""
    conn = seed_db()
    cur = conn.cursor()

    before = cur.execute(
        "EXPLAIN QUERY PLAN SELECT * FROM sales WHERE customer_id = 101"
    ).fetchall()
    cur.execute("CREATE INDEX idx_sales_customer ON sales(customer_id)")
    after = cur.execute(
        "EXPLAIN QUERY PLAN SELECT * FROM sales WHERE customer_id = 101"
    ).fetchall()

    conn.close()
    return {
        "before": [tuple(r) for r in before],
        "after": [tuple(r) for r in after],
    }
