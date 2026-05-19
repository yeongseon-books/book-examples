"""Tests for ep10 in Python 101."""

from en.ep10_stdlib_tour import stdlib_snapshot


def test_stdlib_snapshot() -> None:
    """Test stdlib snapshot."""
    snap = stdlib_snapshot(["x", "x", "y"])
    assert snap["top_word"] == ("x", 2)
    assert snap["suffix"] == ".txt"
