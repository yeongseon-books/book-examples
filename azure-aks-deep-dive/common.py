from __future__ import annotations

from typing import Any

import yaml


def to_yaml(data: dict[str, Any]) -> str:
    return yaml.safe_dump(data, sort_keys=False)


def command_preview(parts: list[str]) -> str:
    return " ".join(parts)
