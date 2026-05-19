import random
import sqlite3
import time
from collections.abc import Iterable
from datetime import date, timedelta


def gen_synthetic_sales(
    n: int, seed: int = 42
) -> Iterable[tuple[str, str, str, float, int, str]]:
    rnd = random.Random(seed)
    products = ["P100", "P200", "P300"]
    regions = ["KR-Seoul", "KR-Busan", "US-CA"]
    start = date(2025, 1, 1)
    for i in range(1, n + 1):
        day = start + timedelta(days=rnd.randint(0, 420))
        yield (
            day.isoformat(),
            rnd.choice(products),
            f"C{(i % 50) + 1:03d}",
            round(rnd.uniform(10, 500), 2),
            rnd.randint(1, 5),
            rnd.choice(regions),
        )


def make_dw(n: int = 500, seed: int = 42) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript(
        """
        CREATE TABLE dim_date(date_key INTEGER PRIMARY KEY, full_date TEXT UNIQUE, year INTEGER, month INTEGER);
        CREATE TABLE dim_product(product_key INTEGER PRIMARY KEY AUTOINCREMENT, product_id TEXT UNIQUE, category TEXT);
        CREATE TABLE dim_customer(customer_key INTEGER PRIMARY KEY AUTOINCREMENT, customer_id TEXT UNIQUE, region TEXT);
        CREATE TABLE fact_sales(sale_id INTEGER PRIMARY KEY AUTOINCREMENT, date_key INTEGER, product_key INTEGER, customer_key INTEGER, amount REAL, qty INTEGER);
        """
    )
    for d, pid, cid, amount, qty, region in gen_synthetic_sales(n, seed):
        date_key = int(d.replace("-", ""))
        y, m, _ = d.split("-")
        c.execute(
            "INSERT OR IGNORE INTO dim_date VALUES (?,?,?,?)",
            (date_key, d, int(y), int(m)),
        )
        c.execute(
            "INSERT OR IGNORE INTO dim_product(product_id, category) VALUES (?,?)",
            (pid, "Beverage" if pid in {"P100", "P200"} else "Snack"),
        )
        c.execute(
            "INSERT OR IGNORE INTO dim_customer(customer_id, region) VALUES (?,?)",
            (cid, region),
        )
        product_key = c.execute(
            "SELECT product_key FROM dim_product WHERE product_id=?", (pid,)
        ).fetchone()[0]
        customer_key = c.execute(
            "SELECT customer_key FROM dim_customer WHERE customer_id=?", (cid,)
        ).fetchone()[0]
        c.execute(
            "INSERT INTO fact_sales(date_key, product_key, customer_key, amount, qty) VALUES (?,?,?,?,?)",
            (date_key, product_key, customer_key, amount, qty),
        )
    conn.commit()
    return conn


def time_query(
    conn: sqlite3.Connection, query: str, params: tuple = ()
) -> tuple[list[tuple], float]:
    s = time.perf_counter()
    rows = conn.execute(query, params).fetchall()
    return rows, time.perf_counter() - s
