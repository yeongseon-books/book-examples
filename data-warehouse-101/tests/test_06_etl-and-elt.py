"""Tests for 06 etl-and-elt in Data Warehouse 101."""

from conftest import load_episode


def test_06_etl_and_elt():
    """Test 06 etl and elt."""
    mod = load_episode("ko", "06-etl-and-elt.py")
    res = mod["run_demo"]()
    assert res["etl"] == res["elt"]
