"""Tests for 01 what-is-data-warehouse in Data Warehouse 101."""

from conftest import load_episode


def test_01_what_is_data_warehouse():
    """Test 01 what is data warehouse."""
    mod = load_episode("ko", "01-what-is-data-warehouse.py")
    res = mod["run_demo"]()
    assert res["months"] > 0 and res["total_revenue"] > 0
