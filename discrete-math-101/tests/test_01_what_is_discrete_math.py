"""Tests for 01 what is discrete math in Discrete Math 101."""

import importlib.util
from pathlib import Path


def load(p):
    """Load."""
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_tour_keys():
    """Test tour keys."""
    m = load(Path("ko/01-what-is-discrete-math.py"))
    d = m.discrete_tour()
    assert d["boolean"] is True and "union" in d["set_ops"]
