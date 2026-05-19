from en.ep07_postmortem_validator import blameless_issues, validate_sections


def test_ep07_postmortem_validator():
    doc = "## Summary\n## Impact\n## Timeline\n## Root Cause\n## Actions\n"
    assert validate_sections(doc) == []
    assert blameless_issues("This was careless") == ["careless"]
