"""Tests for ep02 in Python 101."""

from en.ep02_variables_types import calculate_basics


def test_calculate_basics() -> None:
    """Test calculate basics."""
    result = calculate_basics(8, 2)
    assert result["sum"] == 10
    assert result["quotient"] == 4
