"""Azure App Service Deep Dive - Episode 1: Sandbox profile."""

from __future__ import annotations

from common import sandbox_constraints


def run(os_type: str) -> dict[str, object]:
    # Compare worker execution boundaries for Windows and Linux.
    """Run."""
    return sandbox_constraints(os_type)


if __name__ == "__main__":
    print(run("windows"))
