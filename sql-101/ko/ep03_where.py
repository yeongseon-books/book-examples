"""Sql 101 - Episode 3: Where."""

from common import seed_db


def run_demo():
    """Run demo."""
    conn = seed_db()
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT name
        FROM employees
        WHERE (department_id IN (2, 4) OR department_id IS NULL)
          AND salary BETWEEN 70000 AND 95000
          AND name LIKE '%a%'
          AND name <> 'Diana'
        ORDER BY name
        """
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]
