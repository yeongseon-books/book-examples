"""Tests for ep06 in Secure Coding 101."""

from en import ep06_secret_management


def test_ep06_secret_mgmt():
    """Test ep06 secret mgmt."""
    result = ep06_secret_management.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
