"""에피소드 04: Dispatcher가 호출을 워커로 라우팅하는 흐름을 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import route_invocation


def run(trigger: str) -> dict[str, object]:
    """Run."""
    payload = {"invocation_id": "abc-123", "function_id": "f1"}
    response = route_invocation(trigger, payload)
    return {"status": response.status_code, "body": response.body}


if __name__ == "__main__":
    print(run("http"))
