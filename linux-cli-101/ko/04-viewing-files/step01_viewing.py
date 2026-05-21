"""Linux Cli 101 - 4편: viewing files 예제."""

from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    """Run."""
    ws = make_temp_workspace("ep04-")
    (ws / "data.txt").write_text("line1\nline2\nline3\n", encoding="utf-8")
    head = run_cmd(ws, "head", "-n", "2", "data.txt")
    return {"code": head.returncode, "stdout": head.stdout}
