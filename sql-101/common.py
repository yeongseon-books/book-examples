"""Shared utilities and domain models for Sql 101."""

import sqlite3


def seed_db() -> sqlite3.Connection:
    """Seed db."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.executescript(
        """
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER,
            salary INTEGER NOT NULL,
            hire_date TEXT NOT NULL,
            manager_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id),
            FOREIGN KEY (manager_id) REFERENCES employees(id)
        );

        CREATE TABLE sales (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            sold_at TEXT NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees(id)
        );
        """
    )

    cur.executemany(
        "INSERT INTO departments(id, name) VALUES (?, ?)",
        [
            (1, "Engineering"),
            (2, "Sales"),
            (3, "HR"),
            (4, "Support"),
        ],
    )

    cur.executemany(
        """
        INSERT INTO employees(id, name, department_id, salary, hire_date, manager_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (1, "Alice", 1, 120000, "2021-01-10", None),
            (2, "Bob", 2, 90000, "2021-02-12", 1),
            (3, "Charlie", 2, 95000, "2022-03-15", 2),
            (4, "Diana", 3, 80000, "2023-07-01", 1),
            (5, "Evan", None, 70000, "2023-08-20", 1),
            (6, "Fiona", 4, 85000, "2024-01-05", 1),
        ],
    )

    cur.executemany(
        "INSERT INTO sales(id, employee_id, customer_id, amount, sold_at) VALUES (?, ?, ?, ?, ?)",
        [
            (1, 2, 101, 300, "2024-01-15"),
            (2, 2, 102, 200, "2024-01-20"),
            (3, 3, 101, 150, "2024-02-01"),
            (4, 3, 103, 400, "2024-02-10"),
            (5, 2, 104, 250, "2024-03-05"),
            (6, 6, 105, 500, "2024-03-07"),
            (7, 6, 101, 220, "2024-03-15"),
            (8, 2, 106, 100, "2024-04-01"),
        ],
    )

    conn.commit()
    return conn
