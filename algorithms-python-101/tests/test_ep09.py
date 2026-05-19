"""Tests for ep09 in Algorithms Python 101."""

from tests.conftest import load_module


def test_activity_selection() -> None:
    """Test activity selection."""
    mod = load_module("ko/09-greedy-algorithms/step01_greedy.py", "ep09")
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 11), (12, 16)]
    assert mod.activity_selection(activities) == [(1, 4), (5, 7), (8, 11), (12, 16)]
