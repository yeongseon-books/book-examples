import sqlite3

from common import assert_demo


def setup_db(conn):
    conn.execute("create table users(id integer primary key, name text)")
    conn.execute("insert into users(name) values ('alice')")
    conn.execute("insert into users(name) values ('bob')")


def insecure_find_user(conn, name: str):
    q = f"select name from users where name = '{name}'"
    return list(conn.execute(q))


def safe_find_user(conn, name: str):
    q = "select name from users where name = ?"
    return list(conn.execute(q, (name,)))


def run_demo():
    conn = sqlite3.connect(":memory:")
    setup_db(conn)
    payload = "' OR 1=1 --"
    insecure_detected = len(insecure_find_user(conn, payload)) == 2
    safe_ok = (
        len(safe_find_user(conn, payload)) == 0
        and len(safe_find_user(conn, "alice")) == 1
    )
    return assert_demo(insecure_detected, safe_ok)
