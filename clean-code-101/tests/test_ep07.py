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


def test_ep07_comments_docs() -> None:
    m = load("07-comments-and-docs/step01_comments_and_docs.py")
    assert m.is_paid({"status": "PAID"}) is True
    assert m.discount(100, 0.25) == 75
    with pytest.raises(ValueError):
        m.discount(100, 2)
