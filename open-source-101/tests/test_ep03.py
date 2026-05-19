"""Tests for ep03 in Open Source 101."""

from common import (
    parse_markdown_front_matter,
)
from en.ep03_issue_template_parser import run_example as run_en
from ko.ep03_issue_template_parser import run_example as run_ko


def test_ep03_behavior():
    """Test ep03 behavior."""
    result = run_ko()
    assert result.get("name") == "Bug report"
    assert run_en().get("about") == "Report a reproducible bug"
    assert parse_markdown_front_matter("no front matter") == {}
