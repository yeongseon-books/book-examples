"""Tests for ep06 in Alembic 101."""


# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep06_data_migration(load_module):
    """Test ep06 data migration."""
    m = load_module("ko/06-data-migrations/step01_data_backfill.py", "ep06")
    assert m.backfill_tier(batch_size=2) == 5
