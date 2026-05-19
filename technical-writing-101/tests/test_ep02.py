"""Tests for ep02 in Technical Writing 101."""

from en.ep02_reader_profile import analyze


def test_ep02_profile_advanced():
    """Test ep02 profile advanced."""
    res = analyze("fixtures/ep02_profile.md")
    assert res["audience"] == "advanced"
