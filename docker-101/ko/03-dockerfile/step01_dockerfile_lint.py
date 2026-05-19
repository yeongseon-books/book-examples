from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import DockerfileLinter

# 한국어 주석: 오프라인 검증 예제입니다.


def run() -> dict[str, object]:
    dockerfile = """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
USER 1000
CMD ["python", "app.py"]
"""
    issues = DockerfileLinter().lint(dockerfile)
    return {"success": len(issues) == 0, "issues": issues}


if __name__ == "__main__":
    print(run())
