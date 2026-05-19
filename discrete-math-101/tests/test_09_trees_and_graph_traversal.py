import importlib.util
from pathlib import Path


def load(p):
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_topological_sort_valid_order():
    m = load(Path("ko/09-trees-and-graph-traversal.py"))
    g = {1: [2, 3], 2: [4], 3: [4], 4: []}
    order = m.topo_sort(g)
    pos = {v: i for i, v in enumerate(order)}
    assert pos[1] < pos[2] and pos[1] < pos[3] and pos[2] < pos[4] and pos[3] < pos[4]
