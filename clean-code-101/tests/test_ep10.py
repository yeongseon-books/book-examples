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


def test_ep10_review_rules() -> None:
    m = load("10-good-code-review/step01_good_code_review.py")
    comment = m.classify_comment("SUGG", "Extract subtotal for readability")
    assert comment.level == "SUGG"
    assert m.is_small_pr(120) is True
    with pytest.raises(ValueError):
        m.classify_comment("BAD", "invalid")
