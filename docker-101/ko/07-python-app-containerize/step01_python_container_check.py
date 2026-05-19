from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

from common import DockerfileLinter, HealthcheckVerifier

# 한국어 주석: 오프라인 검증 예제입니다.

def run() -> dict[str, object]:
    dockerfile = """FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN useradd -m -u 1000 appuser
USER appuser
HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD python -c "print('ok')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
    issues = DockerfileLinter().lint(dockerfile)
    has_health = HealthcheckVerifier().has_healthcheck(dockerfile)
    return {"success": len(issues) == 0 and has_health, "issues": issues, "has_healthcheck": has_health}


if __name__ == "__main__":
    print(run())
