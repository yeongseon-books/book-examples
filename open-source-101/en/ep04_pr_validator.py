from __future__ import annotations

from pathlib import Path

from common import (
    validate_pr_description,
)


def run_example() -> object:
    text = Path("fixtures/PR_TEMPLATE.md").read_text(encoding="utf-8")
    return validate_pr_description(text)


if __name__ == "__main__":
    print(run_example())
