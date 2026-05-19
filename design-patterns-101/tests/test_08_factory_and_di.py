"""Tests for 08 factory and di in Design Patterns 101."""

import importlib.util
from pathlib import Path


def load():
    """Load."""
    p = Path(__file__).resolve().parents[1] / "ko/08-factory-and-di.py"
    s = importlib.util.spec_from_file_location("ep08", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_factory_and_di_with_mock_injection():
    """Test factory and di with mock injection."""
    m = load()

    class MockPlugin(m.Plugin):
        """Mock plugin."""

        def run(self, text):
            """Run."""
            return f"mock:{text}"

    c = m.Container()
    c.register(m.Plugin, lambda: MockPlugin())
    svc = m.Service(c.resolve(m.Plugin))
    assert svc.process("abc") == "mock:abc"
    assert m.plugin_factory("upper").run("ab") == "AB"
