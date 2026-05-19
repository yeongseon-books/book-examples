"""Tests for ep08 in Algorithms 101."""

from conftest import load_module

ko = load_module("ko/08-graph-algorithms/step01_bfs_shortest_reach.py", "ko_ep08")


def test_ep08_bfs_dist() -> None:
    """Test ep08 bfs dist."""
    dist = ko.run()["dist"]
    assert dist[0] == 0
    assert dist[4] == 3
