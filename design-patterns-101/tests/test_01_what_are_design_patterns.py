import importlib.util
from pathlib import Path


def load(name):
    p = Path(__file__).resolve().parents[1] / "ko" / f"{name}.py"
    s = importlib.util.spec_from_file_location(name.replace("-", "_"), p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_equivalent_behavior():
    m = load("01-what-are-design-patterns")
    assert m.send_without_pattern("email", "x") == m.send_with_pattern("email", "x")
