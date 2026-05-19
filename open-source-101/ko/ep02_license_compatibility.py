"""Open Source 101 - Episode 2: License compatibility."""

from __future__ import annotations

from common import (
    is_license_compatible,
)


def run_example() -> object:
    """Run example."""
    return is_license_compatible("MIT", "Apache-2.0")


if __name__ == "__main__":
    print(run_example())
