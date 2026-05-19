from common import seed_db


def run_demo():
    conn = seed_db()
    cur = conn.cursor()
    rows = cur.execute(
        """
        WITH emp_sales AS (
            SELECT employee_id, sold_at, amount
            FROM sales
        )
        SELECT
            employee_id,
            sold_at,
            amount,
            ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY sold_at) AS rn,
            RANK() OVER (ORDER BY amount DESC) AS rnk,
            DENSE_RANK() OVER (ORDER BY amount DESC) AS drnk,
            LAG(amount) OVER (PARTITION BY employee_id ORDER BY sold_at) AS prev_amount,
            LEAD(amount) OVER (PARTITION BY employee_id ORDER BY sold_at) AS next_amount,
            SUM(amount) OVER (PARTITION BY employee_id ORDER BY sold_at ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_sum
        FROM emp_sales
        ORDER BY employee_id, sold_at
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
