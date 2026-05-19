"""Tests for 05 linked lists in Data Structures Python 101."""

import importlib.util
import sys
from pathlib import Path


def load(path: str):
    """Load."""
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = load(str(Path(__file__).resolve().parents[1] / "ko/05-linked-lists.py"))


def test_tiny_linked_list_builds_chain():
    """Test tiny linked list builds chain."""
    head = M.tiny_singly_linked_list([1, 2, 3])
    assert head is not None and head.value == 1
    assert head.next is not None and head.next.value == 2


def test_deque_rotation_and_sliding_window():
    """Test deque rotation and sliding window."""
    assert M.deque_rotation([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert M.sliding_window([1, 2, 3, 4, 5], 3) == [6, 9, 12]
