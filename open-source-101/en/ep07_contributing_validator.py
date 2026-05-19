"""Open Source 101 - Episode 7: Contributing validator."""

from __future__ import annotations

from pathlib import Path

from common import (
    validate_contributing_files,
)


def run_example() -> object:
    """Run example."""
    contributing = Path("fixtures/CONTRIBUTING.md").read_text(encoding="utf-8")
    has_coc = Path("fixtures/CODE_OF_CONDUCT.md").exists()
    return validate_contributing_files(contributing, has_coc)


if __name__ == "__main__":
    print(run_example())
