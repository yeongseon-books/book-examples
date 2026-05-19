import importlib.util
from pathlib import Path


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep01_clean_code_signals() -> None:
    m = load("01-what-is-clean-code/step01_clean_code_basics.py")
    assert m.total_with_tax(100, 0.1) == 110.00000000000001
    assert m.readability_signals(18, 2, 2)["short_function"] is True
