"""Tests for ep03 in Python 101."""

from en.ep03_strings_formatting import normalize_words


def test_normalize_words() -> None:
    """Test normalize words."""
    assert normalize_words(" A, b, ,C ") == ["a", "b", "c"]
