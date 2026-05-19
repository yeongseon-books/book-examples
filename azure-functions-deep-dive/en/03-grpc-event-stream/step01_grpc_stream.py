"""Episode 03: Simulates EventStream handshake and capability negotiation."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import startup_handshake


def run() -> dict[str, object]:
    """Run."""
    host_capabilities = {"RpcHttpBodyOnly", "SharedMemoryDataTransfer"}
    worker_capabilities = {"SharedMemoryDataTransfer", "TypedDataCollection"}
    return startup_handshake("worker-42", host_capabilities, worker_capabilities)


if __name__ == "__main__":
    print(run())
