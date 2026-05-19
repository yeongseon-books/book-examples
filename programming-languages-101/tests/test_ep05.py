"""Tests for ep05 in Programming Languages 101."""

from ko.ep05_closures import make_counter, partial_add


def test_ep05_closures_work():
    """Test ep05 closures work."""
    c = make_counter(5)
    assert c() == 6 and c() == 7
    assert partial_add(10)(3) == 13
