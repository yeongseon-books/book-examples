"""Tests for 03 data structures and algorithms in Computer Science Major 101."""

from conftest import load_module


def test_linked_list_and_bst_behaviors() -> None:
    """Test linked list and bst behaviors."""
    mod = load_module("ko/03-data-structures-and-algorithms.py")

    linked = mod.LinkedList()
    linked.insert_front(1)
    linked.insert_front(2)
    assert linked.find(1)
    assert linked.delete(1)
    assert not linked.find(1)

    bst = mod.BinarySearchTree()
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(15, "fifteen")
    assert bst.find(15) == "fifteen"
    bst.delete(15)
    assert bst.find(15) is None
