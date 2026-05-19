"""Shared utilities and domain models for Azure Functions Deep Dive."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MockHttpRequest:
    """Mock http request."""

    method: str
    url: str
    body: bytes


@dataclass
class MockHttpResponse:
    """Mock http response."""

    status_code: int
    body: str


AZ_CLI_SAMPLE = "az functionapp log tail -n my-func -g my-rg"
FUNC_CLI_SAMPLE = "func start --verbose"


def parse_host_json(raw: dict[str, object], env: dict[str, str]) -> dict[str, object]:
    """Parse host json."""
    timeout = raw.get("functionTimeout", "00:05:00")
    env_timeout = env.get("AzureFunctionsJobHost__functionTimeout")
    return {
        "function_timeout": env_timeout or timeout,
        "worker_process_count": int(env.get("FUNCTIONS_WORKER_PROCESS_COUNT", "1")),
    }


def resolve_worker_configs(configs: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    """Resolve worker configs."""
    return {item["language"]: item for item in configs}


def startup_handshake(
    worker_id: str, host_capabilities: set[str], worker_capabilities: set[str]
) -> dict[str, object]:
    """Startup handshake."""
    negotiated = sorted(host_capabilities.intersection(worker_capabilities))
    return {
        "start_stream": {"worker_id": worker_id},
        "negotiated_capabilities": negotiated,
    }


def fan_out_fan_in(tasks: list[int]) -> int:
    """Fan out fan in."""
    return sum(value * 2 for value in tasks)


def route_invocation(trigger: str, payload: dict[str, object]) -> MockHttpResponse:
    """Route invocation."""
    req = MockHttpRequest(
        method="POST", url=f"/api/{trigger}", body=str(payload).encode()
    )
    if trigger == "http":
        return MockHttpResponse(status_code=200, body=f"ok:{req.url}")
    return MockHttpResponse(status_code=202, body="accepted")


def target_based_instances(
    backlog: int, target_per_instance: int, current_instances: int
) -> int:
    """Target based instances."""
    desired = (backlog + target_per_instance - 1) // target_per_instance
    return max(current_instances, desired)


def specialize_placeholder(
    container_ready: bool, first_request: bool
) -> dict[str, object]:
    """Specialize placeholder."""
    if not container_ready:
        return {"specialized": False, "path": "standby"}
    if first_request:
        return {"specialized": True, "path": "request"}
    return {"specialized": True, "path": "timer"}
