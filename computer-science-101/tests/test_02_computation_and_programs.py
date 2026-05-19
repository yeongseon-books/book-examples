"""Tests for 02 computation and programs in Computer Science 101."""

import importlib.util
from pathlib import Path


def load(name, rel):
    """Load."""
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).parent.parent / rel
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_three_styles_same_result():
    """Test three styles same result."""
    m = load("ep02", "ko/02-computation-and-programs.py")
    assert m.sum_of_squares_imperative(8) == 204
    assert m.sum_of_squares_recursive(8) == 204
    assert m.sum_of_squares_functional(8) == 204
