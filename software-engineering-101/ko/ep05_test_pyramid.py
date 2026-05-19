"""Software Engineering 101 - Episode 5: Test pyramid."""

from __future__ import annotations


def analyze_test_pyramid(paths_text: str) -> dict[str, int]:
    """Analyze test pyramid."""
    counts = {"unit": 0, "integration": 0, "e2e": 0}
    for line in paths_text.splitlines():
        if "/unit/" in line:
            counts["unit"] += 1
        elif "/integration/" in line:
            counts["integration"] += 1
        elif "/e2e/" in line:
            counts["e2e"] += 1
    return counts
