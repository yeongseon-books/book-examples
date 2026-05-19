from common import PasswordHasher


def test_pbkdf2_verify_rejects_wrong_password():
    h = PasswordHasher()
    encoded = h.hash_password_pbkdf2("password123")
    assert not h.verify("wrong-password", encoded)
