"""Tests for 08 data-mart in Data Warehouse 101."""

from conftest import load_episode


def test_08_data_mart():
    """Test 08 data mart."""
    mod = load_episode("ko", "08-data-mart.py")
    res = mod["run_demo"]()
    assert res["mart_rows"] > 0 and abs(res["mart_total"] - res["dw_total"]) < 0.01
