"""Tests for 05 partition-and-clustering in Data Warehouse 101."""

from conftest import load_episode


def test_05_partition_and_clustering():
    """Test 05 partition and clustering."""
    mod = load_episode("ko", "05-partition-and-clustering.py")
    res = mod["run_demo"]()
    assert (
        res["result_rows_all"] == res["result_rows_pruned"]
        and res["scanned_pruned"] < res["scanned_all"]
    )
