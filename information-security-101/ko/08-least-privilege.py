from common import LeastPrivilegeChecker

checker = LeastPrivilegeChecker(
    {"user": {"report": {"read"}}, "admin": {"report": {"read", "delete"}}}
)
print({"allow_user_delete": checker.allow("user", "delete", "report")})
