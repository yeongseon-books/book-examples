"""Tests for ep10 in Secure Coding 101."""

from en import ep10_safe_logging


def test_ep10_safe_logging():
    """Test ep10 safe logging."""
    result = ep10_safe_logging.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
