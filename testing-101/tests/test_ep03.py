from ko.ep03_integration_test import NameValidator, UserRepository, UserService


def test_ep03_integration_register_persists_user(in_memory_db):
    service = UserService(UserRepository(in_memory_db), NameValidator())
    ok = service.register(1, "Alice")
    assert ok is True
    row = in_memory_db.execute("SELECT name FROM users WHERE user_id = 1").fetchone()
    assert row == ("Alice",)
