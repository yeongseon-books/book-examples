"""Tests for ep04 in Python Dbapi 101."""

from en import ep04_parameter_binding_injection as ep


def test_ep04_sql_injection_demo():
    """Test ep04 sql injection demo."""
    result = ep.run_demo()
    assert result["unsafe_count"] >= 1
    assert result["safe_count"] == 0
