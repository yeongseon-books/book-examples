import importlib.util
from pathlib import Path


def load(p):
    s = importlib.util.spec_from_file_location("m", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_power_set_and_injective():
    m = load(Path("ko/03-sets-and-functions.py"))
    ps = m.power_set({"a", "b", "c"})
    assert len(ps) == 8
    f = m.Function({0, 1, 2}, {1, 2, 3}, lambda x: x + 1)
    assert f.is_injective() is True
