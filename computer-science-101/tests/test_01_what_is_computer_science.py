import importlib.util
from pathlib import Path


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).parent.parent / rel
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_binary_increment():
    m = load("ep01", "ko/01-what-is-computer-science.py")
    assert m.increment_binary("110") == "111"
    assert m.increment_binary("111") == "1000"
