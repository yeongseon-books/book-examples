"""Kubernetes 101 - 4편: service 예제."""

from __future__ import annotations

from pathlib import Path

from common import ManifestParser


def run() -> list[dict[str, object]]:
    """Run."""
    path = Path(__file__).with_name("service.yaml")
    return ManifestParser().extract(path.read_text())


if __name__ == "__main__":
    print(run())
