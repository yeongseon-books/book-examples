"""Linux Cli 101 - 1편: what is cli and shell 예제."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep01-")
    (ws / "a.txt").write_text("A\n", encoding="utf-8")
    result = run_cmd(ws, "ls")
    return {"code": result.returncode, "stdout": result.stdout}
