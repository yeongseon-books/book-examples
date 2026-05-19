"""Tests for 03 stacks and queues in Data Structures Python 101."""

import importlib.util
from pathlib import Path


def load(path: str):
    """Load."""
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/03-stacks-and-queues.py"))


def test_balanced_parentheses_cases():
    """Test balanced parentheses cases."""
    assert M.is_balanced_parentheses("([]){}") is True
    assert M.is_balanced_parentheses("([)]") is False
    assert M.is_balanced_parentheses("(((())))") is True


def test_bfs_order():
    """Test bfs order."""
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert M.bfs_order(graph, "A") == ["A", "B", "C", "D"]
