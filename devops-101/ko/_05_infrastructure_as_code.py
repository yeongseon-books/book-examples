"""Devops 101 - Episode 5: Infrastructure as code."""

from __future__ import annotations

import json
from pathlib import Path

ResourceMap = dict[str, dict[str, object]]


def _resource_key(resource: dict[str, object]) -> str:
    """Resource key."""
    return f"{resource['type']}:{resource['name']}"


def apply(desired: list[dict[str, object]], state_file: str) -> dict[str, list[str]]:
    """Apply."""
    current: ResourceMap = {}
    path = Path(state_file)
    if path.exists():
        current = json.loads(path.read_text(encoding="utf-8"))

    desired_map = {_resource_key(resource): resource for resource in desired}

    create = sorted([key for key in desired_map if key not in current])
    destroy = sorted([key for key in current if key not in desired_map])
    update = sorted(
        [
            key
            for key in desired_map
            if key in current and desired_map[key] != current[key]
        ]
    )

    next_state = {**current}
    for key in destroy:
        del next_state[key]
    for key in create + update:
        next_state[key] = desired_map[key]

    path.write_text(json.dumps(next_state, indent=2, sort_keys=True), encoding="utf-8")
    return {"create": create, "update": update, "destroy": destroy}
