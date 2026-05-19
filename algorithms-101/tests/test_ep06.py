"""Tests for ep06 in Algorithms 101."""

from conftest import load_module

ko = load_module("ko/06-dynamic-programming/step01_knapsack_dp.py", "ko_ep06")


def test_ep06_knapsack() -> None:
    """Test ep06 knapsack."""
    assert ko.knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
