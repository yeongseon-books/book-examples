"""Tests for ep06 in Python Package 101."""

from common import ep06_bump_version


def test_ep06_semver_bump_minor_with_prerelease() -> None:
    """Test ep06 semver bump minor with prerelease."""
    assert ep06_bump_version("1.2.3", "minor", prerelease="beta.1") == "1.3.0-beta.1"
