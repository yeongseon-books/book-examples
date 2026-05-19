"""에피소드 03: EventStream 핸드셰이크와 capability 협상을 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import startup_handshake


def run() -> dict[str, object]:
    host_capabilities = {"RpcHttpBodyOnly", "SharedMemoryDataTransfer"}
    worker_capabilities = {"SharedMemoryDataTransfer", "TypedDataCollection"}
    return startup_handshake("worker-42", host_capabilities, worker_capabilities)


if __name__ == "__main__":
    print(run())
