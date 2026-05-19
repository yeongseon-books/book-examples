"""Tests for ep02 in Sql 101."""

from en.ep02_select import run_demo


def test_ep02_select_order_limit_alias():
    """Test ep02 select order limit alias."""
    rows = run_demo()
    assert rows[0]["employee_name"] == "Alice"
    assert len(rows) == 3
