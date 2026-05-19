"""Tests for ep01 in Secure Coding 101."""

from en import ep01_overview


def test_ep01_overview():
    """Test ep01 overview."""
    result = ep01_overview.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
