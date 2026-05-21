"""Linux Cli 101 - Episode 7: process management example."""

from __future__ import annotations

from common import ProcessManager


def run() -> dict[str, int | bool]:
    """Run."""
    pm = ProcessManager()
    proc = pm.spawn_sleep(20)
    running_before = pm.is_running(proc.pid)
    pm.terminate(proc.pid)
    proc.wait(timeout=2)
    running_after = pm.is_running(proc.pid)
    return {
        "pid": proc.pid,
        "running_before": running_before,
        "running_after": running_after,
    }
