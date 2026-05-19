"""Tests for 04 algorithms and complexity in Computer Science 101."""

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


def test_binary_search_grows_logarithmically():
    """Test binary search grows logarithmically."""
    m = load("ep04", "ko/04-algorithms-and-complexity.py")
    rows = m.comparison_table([16, 256, 4096])
    binary_counts = [r[2] for r in rows]
    linear_counts = [r[1] for r in rows]
    assert linear_counts == [16, 256, 4096]
    assert binary_counts[2] <= 13
