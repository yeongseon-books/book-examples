"""Sql 101 - Episode 10: Practical analysis."""

from common import seed_db


def run_demo():
    """Run demo."""
    conn = seed_db()
    cur = conn.cursor()

    top_customers = cur.execute(
        """
        SELECT customer_id, SUM(amount) AS total
        FROM sales
        GROUP BY customer_id
        ORDER BY total DESC
        LIMIT 3
        """
    ).fetchall()

    monthly = cur.execute(
        """
        SELECT substr(sold_at, 1, 7) AS month, SUM(amount) AS total
        FROM sales
        GROUP BY month
        ORDER BY month
        """
    ).fetchall()

    cohort = cur.execute(
        """
        WITH first_month AS (
            SELECT customer_id, MIN(substr(sold_at, 1, 7)) AS cohort_month
            FROM sales
            GROUP BY customer_id
        ),
        activity AS (
            SELECT s.customer_id, f.cohort_month, substr(s.sold_at, 1, 7) AS active_month
            FROM sales s
            JOIN first_month f ON s.customer_id = f.customer_id
        )
        SELECT cohort_month, active_month, COUNT(DISTINCT customer_id) AS customers
        FROM activity
        GROUP BY cohort_month, active_month
        ORDER BY cohort_month, active_month
        """
    ).fetchall()

    conn.close()
    return {
        "top_customers": [dict(r) for r in top_customers],
        "monthly": [dict(r) for r in monthly],
        "cohort": [dict(r) for r in cohort],
    }
