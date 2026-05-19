"""Tests for 07 bi-and-dashboard in Data Warehouse 101."""

from conftest import load_episode


def test_07_bi_and_dashboard():
    """Test 07 bi and dashboard."""
    mod = load_episode("ko", "07-bi-and-dashboard.py")
    res = mod["run_demo"]()
    assert res["total"] >= 0 and len(res["trend"]) > 0 and "#" in res["preview"]
