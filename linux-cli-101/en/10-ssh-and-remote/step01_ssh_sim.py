from __future__ import annotations

from common import SSHSimulator


def run() -> dict[str, object]:
    sim = SSHSimulator()
    sim.add_user_key("deploy", "key-123")
    ok = sim.run("deploy", "key-123", "ls /opt/app")
    fail = sim.run("deploy", "wrong", "ls /opt/app")
    return {"ok": ok, "fail": fail, "commands": sim.command_log}
