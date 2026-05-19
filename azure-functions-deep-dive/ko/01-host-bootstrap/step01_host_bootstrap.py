"""에피소드 01: 호스트 부팅 핵심 흐름을 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import AZ_CLI_SAMPLE, parse_host_json


def run() -> dict[str, object]:
    host_json = {"functionTimeout": "00:05:00"}
    env = {
        "AzureFunctionsJobHost__functionTimeout": "00:02:00",
        "FUNCTIONS_WORKER_PROCESS_COUNT": "2",
    }
    resolved = parse_host_json(host_json, env)
    return {"resolved": resolved, "ops_hint": AZ_CLI_SAMPLE}


if __name__ == "__main__":
    print(run())
