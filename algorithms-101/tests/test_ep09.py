"""Tests for ep09 in Algorithms 101."""

from conftest import load_module

ko = load_module("ko/09-string-algorithms/step01_kmp_search.py", "ko_ep09")


def test_ep09_kmp() -> None:
    """Test ep09 kmp."""
    assert ko.compute_failure("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    assert ko.kmp_search("ababcababcabc", "ababcabc") == 5
