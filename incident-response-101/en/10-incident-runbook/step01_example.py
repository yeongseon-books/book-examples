"""Incident Response 101 - Episode 10: incident runbook example."""

from common import RunbookExecutor


def run() -> list[dict[str, str]]:
    """Run."""
    payload = '{"fail_fast": true, "steps": [{"name": "ack", "success": true}, {"name": "mitigate", "success": false}, {"name": "notify", "success": true}]}'
    executor = RunbookExecutor()
    runbook = executor.load(payload)
    return executor.execute(runbook, {})


if __name__ == "__main__":
    print(run())
