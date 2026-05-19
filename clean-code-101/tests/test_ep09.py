import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep09_refactoring() -> None:
    m = load("09-refactoring-basics/step01_refactoring_basics.py")
    order = m.Order(items=[m.Item(100, 2)], coupon=True, member=True)
    assert m.order_total(order) == 171
