"""Tests for ep03 in Secure Coding 101."""

from en import ep03_authentication


def test_ep03_auth():
    """Test ep03 auth."""
    result = ep03_authentication.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
