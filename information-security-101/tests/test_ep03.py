"""Tests for ep03 in Information Security 101."""

from common import PasswordHasher


def test_pbkdf2_verify_rejects_wrong_password():
    """Test pbkdf2 verify rejects wrong password."""
    h = PasswordHasher()
    encoded = h.hash_password_pbkdf2("password123")
    assert not h.verify("wrong-password", encoded)
