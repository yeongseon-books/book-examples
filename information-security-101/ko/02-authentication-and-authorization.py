from common import AuthSystem

auth = AuthSystem()
auth.register("alice", "password123", "user")
print(
    {
        "authenticated": auth.authenticate("alice", "password123"),
        "can_delete": auth.authorize("alice", "delete"),
    }
)
