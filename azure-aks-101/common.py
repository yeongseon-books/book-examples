from __future__ import annotations

from pathlib import Path
import shlex
from typing import Any

import yaml


def shell_join(parts: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in parts)


def build_az_aks_create_command(
    resource_group: str, cluster_name: str, node_count: int
) -> list[str]:
    return [
        "az",
        "aks",
        "create",
        "--resource-group",
        resource_group,
        "--name",
        cluster_name,
        "--node-count",
        str(node_count),
        "--generate-ssh-keys",
    ]


def dump_yaml(document: dict[str, Any]) -> str:
    return yaml.safe_dump(document, sort_keys=False)


def load_yaml(text: str) -> dict[str, Any]:
    loaded = yaml.safe_load(text)
    if not isinstance(loaded, dict):
        raise ValueError("YAML root must be a mapping")
    return loaded


def write_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path
