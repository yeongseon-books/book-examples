from __future__ import annotations

from pathlib import Path

from common import (
    parse_markdown_front_matter,
)


def run_example() -> object:
    text = Path("fixtures/ISSUE_TEMPLATE.md").read_text(encoding="utf-8")
    return parse_markdown_front_matter(text)


if __name__ == "__main__":
    print(run_example())
