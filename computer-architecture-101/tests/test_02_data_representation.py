"""Tests for 02 data representation in Computer Architecture 101."""

from conftest import load_module

mod = load_module("ko/02-data-representation.py", "ep02")


def test_twos_complement() -> None:
    """Test twos complement."""
    assert mod.to_twos_complement(-5, 8) == "11111011"


def test_float_decomposition_sign() -> None:
    """Test float decomposition sign."""
    sign, _, _ = mod.decompose_float64(-0.5)
    assert sign == 1
