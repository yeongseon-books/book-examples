from pathlib import Path

from common import ep09_extract_docstrings


def test_ep09_docstring_google_style_detection() -> None:
    out = ep09_extract_docstrings(Path("fixtures/sample_module.py"))
    assert out["google_style_count"] >= 1
