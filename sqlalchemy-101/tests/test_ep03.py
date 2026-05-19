"""Tests for ep03 in Sqlalchemy 101."""

from ko import ep03_core_crud


def test_ep03_core_crud() -> None:
    """Test ep03 core crud."""
    result = ep03_core_crud.run()
    assert result["before"] == "alice"
    assert result["after"] == "alice-updated"
    assert result["count"] == "0"
