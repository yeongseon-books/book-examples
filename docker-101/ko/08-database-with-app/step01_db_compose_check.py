from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

from common import ComposeValidator

# 한국어 주석: 오프라인 검증 예제입니다.

def run() -> dict[str, object]:
    compose_yaml = """services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d app"]
  migrate:
    image: myapi:1.0
    depends_on:
      db:
        condition: service_healthy
  web:
    image: myapi:1.0
    depends_on:
      migrate:
        condition: service_completed_successfully
"""
    issues = ComposeValidator().validate(compose_yaml)
    return {"success": len(issues) == 0, "issues": issues}


if __name__ == "__main__":
    print(run())
