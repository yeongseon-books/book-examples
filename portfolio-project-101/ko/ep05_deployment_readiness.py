from __future__ import annotations

from pathlib import Path

from common import contains_port_binding, read_text


def check_deployment_readiness(project_root: str | Path) -> dict[str, bool]:
    root = Path(project_root)
    req_path = root / "requirements.txt"
    app_path = root / "app.py"
    req_text = read_text(req_path) if req_path.exists() else ""
    app_text = read_text(app_path) if app_path.exists() else ""
    return {
        "has_dockerfile": (root / "Dockerfile").exists(),
        "has_env_example": (root / ".env.example").exists(),
        "binds_0_0_0_0": contains_port_binding(app_text),
        "requirements_pinned": all(
            "==" in line for line in req_text.splitlines() if line.strip()
        ),
    }
