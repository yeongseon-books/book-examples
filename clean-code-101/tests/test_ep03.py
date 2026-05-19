import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep03_small_functions() -> None:
    m = load("03-small-functions/step01_small_functions.py")
    item = m.LineItem(price=100, qty=2)
    assert m.line_total(item) == 200
    assert m.in_range(5, m.Range(1, 10)) is True
