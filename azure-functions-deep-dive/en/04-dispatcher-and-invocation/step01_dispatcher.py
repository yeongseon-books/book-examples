"""Episode 04: Simulates how dispatcher routes invocation to a worker."""

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
