"""Docker 101 - Episode 1: Image container lifecycle."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

# 한국어 주석: 오프라인 검증 예제입니다.


def run() -> dict[str, object]:
    """Run."""
    lifecycle = ["created", "running", "stopped", "removed"]
    immutable_image = True
    return {"success": True, "lifecycle": lifecycle, "immutable_image": immutable_image}


if __name__ == "__main__":
    print(run())
