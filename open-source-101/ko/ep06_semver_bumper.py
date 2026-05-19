from __future__ import annotations

from common import (
    bump_semver,
)


def run_example() -> object:
    return bump_semver("1.2.3", "minor")


if __name__ == "__main__":
    print(run_example())
