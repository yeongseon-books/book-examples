"""Tests for 03 structural patterns in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/03-structural-patterns.py"
    s = importlib.util.spec_from_file_location("ep03", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_structural_examples():
    """Test structural examples."""
    m = load()
    assert m.WriterAdapter(m.LegacyWriter()).log("hi")["message"] == "hi"
    assert m.Folder([m.File(3), m.File(4)]).size() == 7
    real = m.DataSource()
    proxy = m.CacheProxy(real)
    proxy.get("a")
    proxy.get("a")
    assert real.calls == 1
