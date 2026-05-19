"""Tests for ep03 in Algorithms 101."""

from conftest import load_module

ko = load_module(
    "ko/03-search-algorithms/step01_binary_search_and_bounds.py", "ko_ep03"
)


def test_ep03_bounds_and_count() -> None:
    """Test ep03 bounds and count."""
    result = ko.run()
    assert result["lb"] == 1
    assert result["ub"] == 4
    assert result["count"] == 3
