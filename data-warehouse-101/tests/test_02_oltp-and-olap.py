"""Tests for 02 oltp-and-olap in Data Warehouse 101."""

from conftest import load_episode


def test_02_oltp_and_olap():
    """Test 02 oltp and olap."""
    mod = load_episode("ko", "02-oltp-and-olap.py")
    res = mod["run_demo"]()
    assert res["oltp_one_row"] == 1 and res["olap_groups"] > 0
