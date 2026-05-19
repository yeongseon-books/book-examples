"""Tests for ep02 in Math For Cs 101."""

from common import truth_table

from tests.conftest import load_module


def test_ep02_truth_table_and_rows():
    """Test ep02 truth table and rows."""
    m = load_module("ko/02-logic-and-proofs/step01_logic_and_proofs.py")
    rows = truth_table(m.and_op)
    assert len(rows) == 4
    assert m.sum_induction_identity(100)
