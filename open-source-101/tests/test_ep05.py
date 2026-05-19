"""Tests for ep05 in Open Source 101."""

from common import (
    score_readme,
)
from en.ep05_readme_scorer import run_example as run_en
from ko.ep05_readme_scorer import run_example as run_ko


def test_ep05_behavior():
    """Test ep05 behavior."""
    assert run_ko() == 100
    assert run_en() == 100
    assert score_readme("# only title") == 0
