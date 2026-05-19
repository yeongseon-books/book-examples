"""Information Security 101 - Episode 2: Authentication and authorization."""

from common import AuthSystem

auth = AuthSystem()
auth.register("bob", "password123", "admin")
print(
    {
        "authenticated": auth.authenticate("bob", "password123"),
        "can_delete": auth.authorize("bob", "delete"),
    }
)
