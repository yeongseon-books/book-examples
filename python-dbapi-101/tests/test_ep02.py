"""Tests for ep02 in Python Dbapi 101."""

from en import ep02_connection_cursor_lifecycle as ep


def test_ep02_connection_cursor_lifecycle():
    """Test ep02 connection cursor lifecycle."""
    result = ep.run_demo()
    assert result["selected"] == 1
