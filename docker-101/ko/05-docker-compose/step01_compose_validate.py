"""Docker 101 - Episode 1: Compose validate."""

from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import ComposeValidator

# 한국어 주석: 오프라인 검증 예제입니다.


def run() -> dict[str, object]:
    """Run."""
    compose_yaml = """services:
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
"""
    issues = ComposeValidator().validate(compose_yaml)
    return {"success": len(issues) == 0, "issues": issues}


if __name__ == "__main__":
    print(run())
