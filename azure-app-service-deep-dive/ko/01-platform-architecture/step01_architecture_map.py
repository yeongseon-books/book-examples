"""Azure App Service Deep Dive - Episode 1: Architecture map."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import architecture_layers


def run() -> dict[str, str]:
    # App Service의 핵심 박스를 요약합니다.
    """Run."""
    layers = architecture_layers()
    return {
        "front_end": layers.front_end,
        "worker": layers.worker,
        "storage": layers.storage,
        "scm": layers.scm,
    }


if __name__ == "__main__":
    print(run())
