from __future__ import annotations

from common import make_temp_workspace, run_cmd


def run() -> dict[str, str | int]:
    ws = make_temp_workspace("ep03-")
    target = ws / "secret.txt"
    target.write_text("top-secret\n", encoding="utf-8")
    run_cmd(ws, "chmod", "600", "secret.txt")
    st = target.stat()
    mode = oct(st.st_mode & 0o777)
    return {"code": 0, "mode": mode}
