"""Tests for ep06 in Sqlalchemy 101."""

from ko import ep06_relationships


def test_ep06_relationships() -> None:
    """Test ep06 relationships."""
    post_count, tag_count = ep06_relationships.run()
    assert post_count == 1
    assert tag_count == 1
