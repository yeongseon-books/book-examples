import importlib.util
from pathlib import Path


def load(p):
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_edit_distance_and_dijkstra():
    m = load(Path("ko/10-discrete-math-and-algorithms.py"))
    assert m.edit_distance("kitten", "sitting") == 3
    dist = m.dijkstra({"A": [("B", 2), ("C", 5)], "B": [("C", 1)]}, "A")
    assert dist["C"] == 3
