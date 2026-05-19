"""Tests for 05 strategy pattern in Design Patterns 101."""

import importlib.util
from pathlib import Path

import pytest


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/05-strategy-pattern.py"
    s = importlib.util.spec_from_file_location("ep05", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


@pytest.mark.parametrize(
    "strategy,expected",
    [
        ("CreditCardStrategy", 100.0),
        ("PayPalStrategy", 102.0),
        ("BankTransferStrategy", 98.5),
    ],
)
def test_strategies(strategy, expected):
    """Test strategies."""
    m = load()
    processor = m.PaymentProcessor(getattr(m, strategy)())
    assert processor.checkout(100.0) == expected


def test_runtime_switch():
    """Test runtime switch."""
    m = load()
    p = m.PaymentProcessor(m.CreditCardStrategy())
    p.set_strategy(m.BankTransferStrategy())
    assert p.checkout(50.0) == 48.5
