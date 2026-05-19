from __future__ import annotations

import subprocess

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    ws = make_temp_workspace("ep06-")
    (ws / "log.txt").write_text("ok\nerror\nok\n", encoding="utf-8")
    p1 = subprocess.Popen(["cat", "log.txt"], cwd=ws, stdout=subprocess.PIPE, text=True)
    p2 = subprocess.Popen(
        ["grep", "error"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True
    )
    assert p1.stdout is not None
    p1.stdout.close()
    out, _ = p2.communicate(timeout=3)
    run_cmd(ws, "sh", "-c", "echo saved > out.txt")
    return {"code": p2.returncode, "stdout": out}
