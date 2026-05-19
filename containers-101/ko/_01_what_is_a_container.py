"""Containers 101 - Episode 1: What is a container."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VirtualContainer:
    """Virtual container."""

    name: str
    root: str
    host_fs: dict[str, str]

    def list_visible_files(self) -> dict[str, str]:
        """List visible files."""
        prefix = self.root.rstrip("/") + "/"
        visible: dict[str, str] = {}
        for path, content in self.host_fs.items():
            if path == self.root or path.startswith(prefix):
                key = path[len(self.root) :] or "/"
                visible[key] = content
        return visible

    def can_access(self, path: str) -> bool:
        """Can access."""
        p = path if path.startswith("/") else "/" + path
        return p == self.root or p.startswith(self.root.rstrip("/") + "/")


def run_isolation_demo() -> dict[str, object]:
    """Run isolation demo."""
    host = {
        "/sandbox/app/main.py": 'print("hello")',
        "/sandbox/data/config.json": "{}",
        "/etc/shadow": "restricted",
    }
    container = VirtualContainer("web", "/sandbox", host)
    return {
        "visible": container.list_visible_files(),
        "can_read_shadow": container.can_access("/etc/shadow"),
        "can_read_app": container.can_access("/sandbox/app/main.py"),
    }
