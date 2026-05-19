"""Tests for ep08 in Python Dbapi 101."""

from en import ep08_connection_pool as ep


def test_ep08_connection_pool_basic_usage():
    """Test ep08 connection pool basic usage."""
    result = ep.run_demo()
    assert result["count"] >= 0
