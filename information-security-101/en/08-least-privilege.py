from common import LeastPrivilegeChecker

checker = LeastPrivilegeChecker({"reader": {"log": {"read"}}})
print(
    {
        "allow": checker.allow("reader", "read", "log"),
        "deny": checker.allow("reader", "delete", "log"),
    }
)
