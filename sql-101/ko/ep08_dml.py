from common import seed_db


def run_demo():
    conn = seed_db()
    cur = conn.cursor()

    cur.execute("BEGIN")
    cur.execute(
        "INSERT INTO employees(id, name, department_id, salary, hire_date, manager_id) VALUES (7, 'Gina', 2, 91000, '2024-04-05', 2)"
    )
    cur.execute("UPDATE employees SET salary = salary + 5000 WHERE id = 7")
    cur.execute("DELETE FROM sales WHERE id = 8")
    conn.commit()

    gina_salary = cur.execute("SELECT salary FROM employees WHERE id = 7").fetchone()[0]
    sales_count = cur.execute("SELECT COUNT(*) FROM sales").fetchone()[0]

    conn.close()
    return {'gina_salary': gina_salary, 'sales_count': sales_count}
