import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep05_dry() -> None:
    m = load("05-removing-duplication/step01_removing_duplication.py")
    assert m.with_tax(100, 0.1) == 110
    assert m.quota("team") == 10_000
