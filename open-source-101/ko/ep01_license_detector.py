from __future__ import annotations

from pathlib import Path

from common import (
    detect_spdx_license,
)


def run_example() -> object:
    text = Path("fixtures/LICENSE_MIT.txt").read_text(encoding="utf-8")
    return detect_spdx_license(text)


if __name__ == "__main__":
    print(run_example())
