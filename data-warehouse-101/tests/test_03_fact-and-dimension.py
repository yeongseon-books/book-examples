"""Tests for 03 fact-and-dimension in Data Warehouse 101."""

from conftest import load_episode


def test_03_fact_and_dimension():
    """Test 03 fact and dimension."""
    mod = load_episode("ko", "03-fact-and-dimension.py")
    res = mod["run_demo"]()
    assert res["fact_grain"] == "order_line" and res["fact_rows"] >= res["orders"]
