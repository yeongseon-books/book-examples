"""Linux Cli 101 - Episode 1: Ssh sim."""

from __future__ import annotations

from common import SSHSimulator


def run() -> dict[str, object]:
    """Run."""
    sim = SSHSimulator()
    sim.add_user_key("deploy", "key-123")
    ok = sim.run("deploy", "key-123", "ls /opt/app")
    fail = sim.run("deploy", "wrong", "ls /opt/app")
    return {"ok": ok, "fail": fail, "commands": sim.command_log}
