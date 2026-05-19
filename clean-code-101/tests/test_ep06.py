import importlib.util
from pathlib import Path

import pytest


def load(path: str):
    module_path = Path(__file__).resolve().parent.parent / "ko" / path
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep06_error_handling() -> None:
    m = load("06-error-handling/step01_error_handling.py")
    ok = m.parse_int("42")
    bad = m.parse_int("x")
    assert ok.ok is True and ok.value == 42
    assert bad.ok is False and bad.error
    with pytest.raises(ValueError):
        m.transfer(0)
