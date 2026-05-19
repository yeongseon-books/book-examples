"""Tests for ep04 in Algorithms Python 101."""

from tests.conftest import load_module


def test_merge_sort() -> None:
    """Test merge sort."""
    mod = load_module("ko/04-sorting-algorithms/step01_sorting.py", "ep04")
    assert mod.merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
