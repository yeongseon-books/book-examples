"""Tests for 06 system design interview in Developer Career 101."""

from tests.test_01_what_is_developer_career import load


def test_06_url_shortener_spec_has_required_sections():
    """Test 06 url shortener spec has required sections."""
    mod = load("06-system-design-interview.py")
    spec = mod.generate_spec("design url shortener")
    assert mod.is_complete_spec(spec)
