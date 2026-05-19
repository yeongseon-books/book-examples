"""Tests for ep05 in Information Security 101."""

from common import WebRequestSanitizer


def test_csrf_token_check():
    """Test csrf token check."""
    s = WebRequestSanitizer()
    assert s.check_csrf({"X-CSRF": "token1"}, "token1")
    assert not s.check_csrf({"X-CSRF": "token2"}, "token1")
