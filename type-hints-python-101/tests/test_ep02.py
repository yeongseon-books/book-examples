"""Tests for ep02 in Type Hints Python 101."""

from ko.ep02_basic_collections import collection_summary


def test_ep02_collections_runtime() -> None:
    """Test ep02 collections runtime."""
    out = collection_summary([1, 2], {"a": 3}, (4, 5), {"x", "y"})
    assert out["values_total"] == 3
    assert out["tag_count"] == 2
