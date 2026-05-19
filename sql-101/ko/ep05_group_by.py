"""Sql 101 - Episode 5: Group by."""

from common import seed_db


def run_demo():
    """Run demo."""
    conn = seed_db()
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT e.employee_id, COUNT(*) AS order_count, SUM(e.amount) AS total_amount,
               AVG(e.amount) AS avg_amount, MIN(e.amount) AS min_amount, MAX(e.amount) AS max_amount
        FROM sales e
        GROUP BY e.employee_id
        HAVING SUM(e.amount) >= 700
        ORDER BY total_amount DESC
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
