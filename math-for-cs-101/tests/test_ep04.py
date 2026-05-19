from common import bfs
from tests.conftest import load_module


def test_ep04_bfs_shortest_path_property():
    graph={'A':['B','C'],'B':['D'],'C':['D'],'D':[]}
    assert bfs(graph,'A')[:3]==['A','B','C']
    m=load_module('ko/04-graphs/step01_graphs.py')
    assert not m.has_cycle_directed(graph)
