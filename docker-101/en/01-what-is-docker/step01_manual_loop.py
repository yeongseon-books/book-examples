"""Docker 101 - Episode 1: Manual loop."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

# English note: offline validation example.


def run() -> dict[str, object]:
    """Run."""
    report = {
        "question": "Docker가 해결하는 문제",
        "answer": "애플리케이션과 의존성을 동일 환경으로 묶어 환경 표류를 줄입니다."
        if __name__.startswith("ko")
        else "Docker bundles app and dependencies to reduce environment drift.",
        "keywords": ["image", "container", "registry"],
    }
    return {"success": True, "report": report}


if __name__ == "__main__":
    print(run())
