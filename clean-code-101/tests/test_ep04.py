import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep04_conditionals() -> None:
    m = load("04-simplifying-conditionals/step01_simplifying_conditionals.py")
    user = m.User(is_active=True, is_member=True)
    product = m.Product(price=100, in_stock=True)
    assert m.price(user, product) == 90
    assert m.grade(85) == "B"
