"""Tests for 02 creational patterns in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/02-creational-patterns.py"
    s = importlib.util.spec_from_file_location("ep02", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_creational_patterns():
    """Test creational patterns."""
    m = load()
    assert m.MODULE_SINGLETON is m.MODULE_SINGLETON
    assert m.DecoratedSingleton() is m.DecoratedSingleton()
    assert m.ReportFactory().create("pdf").kind == "pdf"
    assert m.MacFactory().button().__class__.__name__ == "MacButton"
    report = m.ReportBuilder().title("T").body("B").footer("F").build()
    assert (report.title, report.body, report.footer) == ("T", "B", "F")
    base = m.Template({"rows": [1]})
    clone = base.clone()
    clone.fields["rows"].append(2)
    assert base.fields["rows"] == [1]
