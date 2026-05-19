"""Tests for ep02 in Information Security 101."""

from common import AuthSystem


def test_rbac_denies_unauthorized_role():
    """Test rbac denies unauthorized role."""
    auth = AuthSystem()
    auth.register("alice", "password123", "user")
    assert auth.authenticate("alice", "password123")
    assert not auth.authorize("alice", "delete")
