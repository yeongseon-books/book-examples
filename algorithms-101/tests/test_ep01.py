"""Tests for ep01 in Algorithms 101."""

from conftest import load_module

ko = load_module("ko/01-what-is-an-algorithm/step01_algorithm_basics.py", "ko_ep01")
en = load_module("en/01-what-is-an-algorithm/step01_algorithm_basics.py", "en_ep01")


def test_ep01_two_sum_hash() -> None:
    """Test ep01 two sum hash."""
    assert ko.run()["pair"] == (0, 1)
    assert en.run()["pair"] == (0, 1)
