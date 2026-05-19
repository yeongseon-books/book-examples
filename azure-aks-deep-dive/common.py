"""Shared utilities and domain models for Azure Aks Deep Dive."""

from __future__ import annotations

from typing import Any

import yaml


def to_yaml(data: dict[str, Any]) -> str:
    """To yaml."""
    return yaml.safe_dump(data, sort_keys=False)


def command_preview(parts: list[str]) -> str:
    """Command preview."""
    return " ".join(parts)
