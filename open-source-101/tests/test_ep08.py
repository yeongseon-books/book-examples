"""Tests for ep08 in Open Source 101."""

from common import (
    Issue,
    triage_issues,
)
from en.ep08_maintainer_triage import run_example as run_en
from ko.ep08_maintainer_triage import run_example as run_ko


def test_ep08_behavior():
    """Test ep08 behavior."""
    result = run_ko()
    assert result == {"bug": 1, "enhancement": 1, "question": 1, "other": 0}
    assert run_en()["bug"] == 1
    assert triage_issues([Issue(id=4, title="misc", labels=[])])["other"] == 1
