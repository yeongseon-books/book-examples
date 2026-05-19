"""Tests for ep07 in Sre 101."""

from en.ep07_postmortem_validator import blameless_issues, validate_sections


def test_ep07_postmortem_validator():
    """Test ep07 postmortem validator."""
    doc = "## Summary\n## Impact\n## Timeline\n## Root Cause\n## Actions\n"
    assert validate_sections(doc) == []
    assert blameless_issues("This was careless") == ["careless"]
