# repositories/user_repo.py
class UserRepository:
    def __init__(self, session):
        self.session = session

    def save(self, user):
        self.session.add(user)
        self.session.flush()
        return user
