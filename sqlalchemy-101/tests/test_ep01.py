"""Tests for ep01 in Sqlalchemy 101."""

from ko import ep01_engine_connection


def test_ep01_engine_connection() -> None:
    """Test ep01 engine connection."""
    assert ep01_engine_connection.run() == 1
