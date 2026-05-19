"""Tests for ep07 in Secure Coding 101."""

from en import ep07_sql_injection


def test_ep07_sqli():
    """Test ep07 sqli."""
    result = ep07_sql_injection.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
