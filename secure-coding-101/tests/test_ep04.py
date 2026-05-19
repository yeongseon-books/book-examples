"""Tests for ep04 in Secure Coding 101."""

from en import ep04_authorization


def test_ep04_authz():
    """Test ep04 authz."""
    result = ep04_authorization.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
