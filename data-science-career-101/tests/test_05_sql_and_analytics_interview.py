from __future__ import annotations

from .conftest import load_module

mod = load_module("ko/05-sql-and-analytics-interview.py")


def test_sql_reference_queries_return_expected_outputs() -> None:
    conn = mod.build_connection()
    queries = mod.sql_questions()
    top_country = mod.run_query(conn, queries["top_country_by_revenue"])
    assert top_country == [("KR", 60)]
    funnel = mod.run_query(conn, queries["funnel_counts"])
    assert funnel == [(3, 2, 1)]
    running = mod.run_query(conn, queries["running_revenue"])
    assert running[-1][1] == 90
