"""Information Security 101 - Episode 8: Least privilege."""

from common import LeastPrivilegeChecker

checker = LeastPrivilegeChecker(
    {"user": {"report": {"read"}}, "admin": {"report": {"read", "delete"}}}
)
print({"allow_user_delete": checker.allow("user", "delete", "report")})
