"""Linux Cli 101 - Episode 1: Cli shell."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep01-")
    (ws / "a.txt").write_text("A\n", encoding="utf-8")
    result = run_cmd(ws, "ls")
    return {"code": result.returncode, "stdout": result.stdout}
