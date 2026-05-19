"""Tests for ep03 in Python Dbapi 101."""

from en import ep03_fetch_patterns as ep


def test_ep03_fetch_patterns_and_executemany():
    """Test ep03 fetch patterns and executemany."""
    result = ep.run_demo()
    assert result["first"] == "Alice"
    assert result["many"] == ["Alice", "Bob"]
    assert result["count"] == 5
