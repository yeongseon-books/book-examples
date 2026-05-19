"""Tests for 10 pythonic patterns in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/10-pythonic-patterns.py"
    s = importlib.util.spec_from_file_location("ep10", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_pythonic_equivalence():
    """Test pythonic equivalence."""
    m = load()
    assert m.classic_iterator([1, 2, 3]) == m.pythonic_iterator([1, 2, 3])
    assert m.strategy_class("add", 3) == m.strategy_function("add", 3)
    assert m.strategy_class("double", 3) == m.strategy_function("double", 3)
    r = m.FileLike()
    with m.managed_file(r) as obj:
        assert obj.opened is True
    assert r.opened is False
