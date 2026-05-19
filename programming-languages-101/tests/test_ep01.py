"""Tests for ep01 in Programming Languages 101."""

from ko.ep01_repl import repl_once


def test_ep01_safe_repl_arith():
    """Test ep01 safe repl arith."""
    assert repl_once("(1+2)*3") == 9
