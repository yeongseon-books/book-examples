from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

from common import DockerfileLinter

# English note: offline validation example.

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
