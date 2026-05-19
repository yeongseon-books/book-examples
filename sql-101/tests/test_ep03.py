"""Tests for ep03 in Sql 101."""

from en.ep03_where import run_demo


def test_ep03_where_predicates():
    """Test ep03 where predicates."""
    names = run_demo()
    assert names == ["Charlie", "Evan", "Fiona"]
