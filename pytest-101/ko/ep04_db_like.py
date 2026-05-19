class InMemoryUserDB:
    def __init__(self) -> None:
        self._users: dict[int, str] = {}

    def add_user(self, user_id: int, name: str) -> None:
        self._users[user_id] = name

    def get_user(self, user_id: int) -> str | None:
        return self._users.get(user_id)

    def clear(self) -> None:
        self._users.clear()
