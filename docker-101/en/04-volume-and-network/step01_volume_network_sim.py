"""Docker 101 - Episode 1: Volume network sim."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

# English note: offline validation example.


def run() -> dict[str, object]:
    """Run."""
    named_volume_persists = True
    bridge_dns = {"api": "10.10.0.2", "db": "10.10.0.3"}
    can_resolve_db = "db" in bridge_dns
    return {
        "success": named_volume_persists and can_resolve_db,
        "bridge_dns": bridge_dns,
    }


if __name__ == "__main__":
    print(run())
