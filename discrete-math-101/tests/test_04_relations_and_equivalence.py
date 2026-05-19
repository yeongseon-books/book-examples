import importlib.util
from pathlib import Path


def load(p):
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_relation_properties():
    m = load(Path("ko/04-relations-and-equivalence.py"))
    r = m.Relation({0, 1, 2}, {(0, 0), (1, 1), (2, 2), (0, 1), (1, 0)})
    assert r.is_reflexive() and r.is_symmetric()
