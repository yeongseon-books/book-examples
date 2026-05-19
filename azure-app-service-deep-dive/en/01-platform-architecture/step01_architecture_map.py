from __future__ import annotations

from common import architecture_layers


def run() -> dict[str, str]:
    # Summarize the core App Service platform boxes.
    layers = architecture_layers()
    return {
        "front_end": layers.front_end,
        "worker": layers.worker,
        "storage": layers.storage,
        "scm": layers.scm,
    }


if __name__ == "__main__":
    print(run())
