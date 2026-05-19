"""Tests for ep08 in Sql 101."""

from en.ep08_dml import run_demo


def test_ep08_dml_and_transaction():
    """Test ep08 dml and transaction."""
    out = run_demo()
    assert out["gina_salary"] == 96000
    assert out["sales_count"] == 7
