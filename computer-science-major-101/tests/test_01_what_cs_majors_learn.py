"""Tests for 01 what cs majors learn in Computer Science Major 101."""

from conftest import load_module


def test_topological_order_respects_prerequisites() -> None:
    """Test topological order respects prerequisites."""
    mod = load_module("ko/01-what-cs-majors-learn.py")
    graph = {
        "math": [],
        "programming": ["math"],
        "systems": ["programming"],
        "data": ["programming"],
        "ai": ["data"],
    }
    order = mod.topological_curriculum_order(graph)
    pos = {course: idx for idx, course in enumerate(order)}
    for course, pres in graph.items():
        for pre in pres:
            assert pos[pre] < pos[course]
