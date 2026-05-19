"""Tests for ep05 in Secure Coding 101."""

from en import ep05_safe_storage


def test_ep05_storage():
    """Test ep05 storage."""
    result = ep05_safe_storage.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
