"""Tests for ep07 in Python 101."""

from en.ep07_modules_packages import compute_pair


def test_compute_pair() -> None:
    """Test compute pair."""
    assert compute_pair(9, 4) == (13, 5)
