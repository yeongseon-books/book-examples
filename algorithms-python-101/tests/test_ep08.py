from tests.conftest import load_module


def test_dijkstra_distances() -> None:
    mod = load_module("ko/08-shortest-path-basics/step01_dijkstra.py", "ep08")
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 3), ("E", 1)],
        "C": [("A", 2), ("E", 5)],
        "D": [("B", 3)],
        "E": [("B", 1), ("C", 5)],
    }
    assert mod.dijkstra(graph, "A")["D"] == 7
