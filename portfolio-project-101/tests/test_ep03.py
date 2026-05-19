from pathlib import Path

from common import read_text
from ko.ep03_readme_linter import lint_readme_sections


def test_ep03_readme_linter() -> None:
    readme = read_text(Path("fixtures/sample_readme.md"))
    ok, missing = lint_readme_sections(readme)
    assert ok is True
    assert missing == []
