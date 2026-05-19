"""Tests for 08 graph theory basics in Discrete Math 101."""

import importlib.util
from pathlib import Path


def load(p):
    """Load."""
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_bipartite_cases():
    """Test bipartite cases."""
    m = load(Path("ko/08-graph-theory-basics.py"))
    k = m.Graph()
    left = ["a1", "a2", "a3"]
    right = ["b1", "b2", "b3"]
    for u in left:
        for v in right:
            k.add_edge(u, v)
    assert k.is_bipartite() is True
    c = m.Graph()
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 1)
    assert c.is_bipartite() is False
