import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep02_naming() -> None:
    m = load("02-naming/step01_naming.py")
    assert m.SECONDS_PER_DAY == 86_400
    assert m.is_empty([]) is True
