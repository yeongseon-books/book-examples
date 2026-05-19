from common import LeastPrivilegeChecker


def test_least_privilege_deny():
    checker = LeastPrivilegeChecker({"user": {"docs": {"read"}}})
    assert checker.allow("user", "read", "docs")
    assert not checker.allow("user", "delete", "docs")
