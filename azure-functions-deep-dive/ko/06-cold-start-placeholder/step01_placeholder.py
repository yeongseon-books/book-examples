"""에피소드 06: placeholder specialization 트리거를 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import FUNC_CLI_SAMPLE, specialize_placeholder


def run(container_ready: bool, first_request: bool) -> dict[str, object]:
    result = specialize_placeholder(
        container_ready=container_ready, first_request=first_request
    )
    result["ops_hint"] = FUNC_CLI_SAMPLE
    return result


if __name__ == "__main__":
    print(run(container_ready=True, first_request=True))
