# 2_di.py
class UserService:
    def __init__(self, repo):
        self.repo = repo

    def register(self, name: str):
        return self.repo.insert({"name": name})
