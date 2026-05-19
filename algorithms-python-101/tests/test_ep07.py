"""Tests for ep07 in Algorithms Python 101."""

from tests.conftest import load_module


def test_bfs_order() -> None:
    """Test bfs order."""
    mod = load_module("ko/07-graph-traversal-bfs-dfs/step01_graph_traversal.py", "ep07")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E", "F"],
        "D": ["B"],
        "E": ["C"],
        "F": ["C"],
    }
    assert mod.bfs(graph, "A") == ["A", "B", "C", "D", "E", "F"]
