from __future__ import annotations


def simulate_invocation(event_name: str) -> list[str]:
    host = "host: trigger detected"
    grpc = "host->worker: invocation request"
    worker = f"worker: handled {event_name}"
    return [host, grpc, worker]


def run() -> dict[str, list[str]]:
    return {"timeline": simulate_invocation("http.hello")}


if __name__ == "__main__":
    print(run())
