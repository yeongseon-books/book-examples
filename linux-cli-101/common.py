"""Shared utilities and domain models for Linux Cli 101."""

from __future__ import annotations

import os
import signal
import subprocess
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path


def make_temp_workspace(prefix: str = "linux-cli-101-") -> Path:
    """Make temp workspace."""
    return Path(tempfile.mkdtemp(prefix=prefix))


def run_cmd(
    cwd: Path, *args: str, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    """Run cmd."""
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        list(args),
        cwd=str(cwd),
        env=merged_env,
        text=True,
        capture_output=True,
        check=False,
    )


@dataclass
class ProcessManager:
    """Process manager."""

    processes: list[subprocess.Popen[str]] = field(default_factory=list)

    def spawn_sleep(self, seconds: int = 30) -> subprocess.Popen[str]:
        """Spawn sleep."""
        proc = subprocess.Popen(["sleep", str(seconds)], text=True)
        self.processes.append(proc)
        return proc

    def is_running(self, pid: int) -> bool:
        """Is running."""
        return Path(f"/proc/{pid}").exists()

    def terminate(self, pid: int) -> None:
        """Terminate."""
        os.kill(pid, signal.SIGTERM)

    def cleanup(self) -> None:
        """Cleanup."""
        for proc in self.processes:
            if proc.poll() is None:
                proc.terminate()
                proc.wait(timeout=2)


@contextmanager
def EnvScope(overrides: dict[str, str]):
    """Env scope."""
    old_values: dict[str, str | None] = {k: os.environ.get(k) for k in overrides}
    os.environ.update(overrides)
    try:
        yield
    finally:
        for key, old in old_values.items():
            if old is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = old


@dataclass
class SSHSimulator:
    """SSH simulator."""

    allowed_keys: dict[str, str] = field(default_factory=dict)
    command_log: list[tuple[str, str]] = field(default_factory=list)

    def add_user_key(self, user: str, public_key: str) -> None:
        """Add user key."""
        self.allowed_keys[user] = public_key

    def connect(self, user: str, private_key: str) -> bool:
        """Connect."""
        expected = self.allowed_keys.get(user)
        return expected is not None and expected == private_key

    def run(self, user: str, private_key: str, command: str) -> dict[str, str | int]:
        """Run."""
        if not self.connect(user, private_key):
            return {"code": 255, "stdout": "", "stderr": "auth failed"}
        self.command_log.append((user, command))
        return {"code": 0, "stdout": f"[{user}] {command}", "stderr": ""}
