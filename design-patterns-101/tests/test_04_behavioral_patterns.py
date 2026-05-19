"""Tests for 04 behavioral patterns in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/04-behavioral-patterns.py"
    s = importlib.util.spec_from_file_location("ep04", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_behavioral_examples():
    """Test behavioral examples."""
    m = load()
    chain = m.AuthHandler(m.RouteHandler())
    assert chain.handle({"path": "/x", "auth": True}) == "route:/x"
    assert m.AddCommand(2, 3).execute() == 5
    assert list(m.Numbers([1, 2])) == [1, 2]
