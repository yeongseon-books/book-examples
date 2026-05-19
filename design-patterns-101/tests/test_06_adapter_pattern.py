"""Tests for 06 adapter pattern in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/06-adapter-pattern.py"
    s = importlib.util.spec_from_file_location("ep06", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_equivalent_records():
    """Test equivalent records."""
    m = load()
    xml = m.XmlLoggerAdapter(m.LegacyXmlLogger()).log("created", "INFO")
    js = m.JsonLoggerAdapter(m.JsonLogger()).log("created", "INFO")
    assert (xml["event"], xml["level"]) == (js["event"], js["level"])
