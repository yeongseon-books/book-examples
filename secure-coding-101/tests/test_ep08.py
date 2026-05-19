"""Tests for ep08 in Secure Coding 101."""

from en import ep08_xss_csrf


def test_ep08_xss_csrf():
    """Test ep08 xss csrf."""
    result = ep08_xss_csrf.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
