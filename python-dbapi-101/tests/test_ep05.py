"""Tests for ep05 in Python Dbapi 101."""

from en import ep05_transactions as ep


def test_ep05_transaction_commit_and_rollback():
    """Test ep05 transaction commit and rollback."""
    result = ep.run_demo()
    assert result["count_after"] == 1
