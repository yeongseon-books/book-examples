"""Tests for ep08 in Alembic 101."""

# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
import pytest


def test_ep08_downgrade_policy(load_module):
    """Test ep08 downgrade policy."""
    m = load_module("ko/08-downgrade-strategy/step01_downgrade_policy.py", "ep08")
    assert m.guarded_downgrade("add_nullable_column") == "downgrade-applied"
    with pytest.raises(m.IrreversibleMigrationError):
        m.guarded_downgrade("drop_column")
