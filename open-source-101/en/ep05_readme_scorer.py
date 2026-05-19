from __future__ import annotations

from pathlib import Path

from common import (
    score_readme,
)


def run_example() -> object:
    text = Path("fixtures/README_SAMPLE.md").read_text(encoding="utf-8")
    return score_readme(text)


if __name__ == "__main__":
    print(run_example())
