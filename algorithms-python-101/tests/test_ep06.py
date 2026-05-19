"""Tests for ep06 in Algorithms Python 101."""

from tests.conftest import load_module


def test_climb_stairs() -> None:
    """Test climb stairs."""
    mod = load_module("ko/06-dynamic-programming-basics/step01_dp.py", "ep06")
    assert mod.climb_stairs(7) == 21
