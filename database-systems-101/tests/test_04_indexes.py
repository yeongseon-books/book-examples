"""Tests for 04 indexes in Database Systems 101."""

from conftest import load_ko_module


def test_index_steps_less_than_full_scan():
    """Test index steps less than full scan."""
    m = load_ko_module("04-indexes.py")
    result = m.benchmark_lookup(n=10_000, seed=1)
    assert result["bst_steps"] < result["scan_steps"]
    assert result["hash_steps"] < result["scan_steps"]
