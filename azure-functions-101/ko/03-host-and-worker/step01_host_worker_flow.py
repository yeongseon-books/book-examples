"""Azure Functions 101 - Episode 1: Host worker flow."""

from __future__ import annotations


def simulate_invocation(event_name: str) -> list[str]:
    """Simulate invocation."""
    host = "host: trigger detected"
    grpc = "host->worker: invocation request"
    worker = f"worker: handled {event_name}"
    return [host, grpc, worker]


def run() -> dict[str, list[str]]:
    """Run."""
    return {"timeline": simulate_invocation("http.hello")}


if __name__ == "__main__":
    print(run())
