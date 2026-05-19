"""Portfolio Project 101 - Episode 2: Trait checklist."""

from __future__ import annotations

REQUIRED_TRAITS = ("solving_real_problem", "scoped", "deployable")


def validate_project_traits(traits: dict[str, bool]) -> tuple[bool, list[str]]:
    """Validate project traits."""
    missing = [key for key in REQUIRED_TRAITS if not traits.get(key, False)]
    return (len(missing) == 0, missing)
