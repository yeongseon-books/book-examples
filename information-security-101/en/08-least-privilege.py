"""Information Security 101 - Episode 8: Least privilege."""

from common import LeastPrivilegeChecker

checker = LeastPrivilegeChecker({"reader": {"log": {"read"}}})
print(
    {
        "allow": checker.allow("reader", "read", "log"),
        "deny": checker.allow("reader", "delete", "log"),
    }
)
