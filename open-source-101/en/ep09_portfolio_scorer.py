from __future__ import annotations

from pathlib import Path

from common import (
    score_portfolio,
)


def run_example() -> object:
    text = Path("fixtures/repos.json").read_text(encoding="utf-8")
    return score_portfolio(text)


if __name__ == "__main__":
    print(run_example())
