"""Tests for ep08 in Information Security 101."""

from common import LeastPrivilegeChecker


def test_least_privilege_deny():
    """Test least privilege deny."""
    checker = LeastPrivilegeChecker({"user": {"docs": {"read"}}})
    assert checker.allow("user", "read", "docs")
    assert not checker.allow("user", "delete", "docs")
