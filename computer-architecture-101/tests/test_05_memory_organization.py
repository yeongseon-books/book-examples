"""Tests for 05 memory organization in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/05-memory-organization.py", "ep05")


def test_hierarchy_access_counters() -> None:
    """Test hierarchy access counters."""
    counters = mod.demo_sequence()
    assert counters["main"] == 1
    assert counters["l1"] == 1
    assert counters["register"] == 1
