"""Tests for ep02 in Sqlalchemy 101."""

from ko import ep02_core_metadata


def test_ep02_core_metadata() -> None:
    """Test ep02 core metadata."""
    assert ep02_core_metadata.run() == ["products"]
