"""Tests for ep04 in Algorithms 101."""

from conftest import load_module

ko = load_module("ko/04-sorting-algorithms/step01_timsort_and_multikey.py", "ko_ep04")


def test_ep04_sort_and_stability() -> None:
    """Test ep04 sort and stability."""
    result = ko.run()
    assert result["sorted_ok"] is True
    assert result["people"] == [("Bob", 25), ("Dan", 25), ("Alice", 30), ("Carol", 30)]
