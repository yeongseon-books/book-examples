"""Azure Aca 101 - Episode 1: Revision model."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import mock_revision_weights


def classify_change(change: str) -> str:
    """Classify change."""
    revision_changes = {"image", "env", "secret", "cpu", "memory", "scale", "dapr"}
    if change in revision_changes:
        return "new_revision"
    if change in {"traffic", "activate", "deactivate", "tag"}:
        return "same_revision"
    raise ValueError("unknown change")


def run() -> dict[str, object]:
    """Run."""
    return {
        "image": classify_change("image"),
        "traffic": classify_change("traffic"),
        "weights": mock_revision_weights("myapi--v1", "myapi--v2", 10),
    }


if __name__ == "__main__":
    print(run())
