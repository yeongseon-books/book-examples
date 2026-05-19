"""Tests for ep06 in Open Source 101."""

from common import (
    bump_semver,
)
from en.ep06_semver_bumper import run_example as run_en
from ko.ep06_semver_bumper import run_example as run_ko


def test_ep06_behavior():
    """Test ep06 behavior."""
    assert run_ko() == "1.3.0"
    assert run_en() == "1.3.0"
    assert bump_semver("1.2.3", "patch") == "1.2.4"
