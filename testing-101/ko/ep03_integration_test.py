class UserRepository:
    def __init__(self, conn):
        self.conn = conn

    def add_user(self, user_id: int, name: str) -> None:
        self.conn.execute(
            "INSERT INTO users(user_id, name) VALUES (?, ?)", (user_id, name)
        )
        self.conn.commit()


class NameValidator:
    def is_valid(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) >= 2


class UserService:
    def __init__(self, repo: UserRepository, validator: NameValidator):
        self.repo = repo
        self.validator = validator

    def register(self, user_id: int, name: str) -> bool:
        if not self.validator.is_valid(name):
            return False
        self.repo.add_user(user_id, name.strip())
        return True
