"""Episode 02: Simulates worker config catalog and multi-process layout."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import resolve_worker_configs


def run() -> dict[str, object]:
    """Run."""
    configs = [
        {"language": "python", "defaultExecutablePath": "python", "entry": "worker.py"},
        {"language": "node", "defaultExecutablePath": "node", "entry": "worker.js"},
    ]
    catalog = resolve_worker_configs(configs)
    return {"worker_count": len(catalog), "python_entry": catalog["python"]["entry"]}


if __name__ == "__main__":
    print(run())
