"""Shared utilities and domain models for Azure Aca 101."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AzureCommand:
    """Azure command."""

    name: str
    args: list[str]

    def render(self) -> str:
        """Render."""
        return " ".join([self.name, *self.args])


def az(*args: str) -> AzureCommand:
    """Az."""
    return AzureCommand("az", list(args))


def required_env(name: str, env: dict[str, str]) -> str:
    """Required env."""
    if name not in env or not env[name].strip():
        raise ValueError(f"missing env: {name}")
    return env[name]


def mock_revision_weights(
    current: str, candidate: str, candidate_percent: int
) -> dict[str, int]:
    """Mock revision weights."""
    if candidate_percent < 0 or candidate_percent > 100:
        raise ValueError("candidate_percent must be between 0 and 100")
    return {current: 100 - candidate_percent, candidate: candidate_percent}


def mock_scale_decision(
    signal: int, threshold: int, min_replicas: int, max_replicas: int
) -> int:
    """Mock scale decision."""
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    if min_replicas < 0 or max_replicas < min_replicas:
        raise ValueError("invalid replica bounds")
    estimated = (signal + threshold - 1) // threshold
    return max(min_replicas, min(max_replicas, estimated))


def mock_log_rows() -> list[dict[str, str]]:
    """Mock log rows."""
    return [
        {"RevisionName_s": "myapi--v1", "Log_s": "INFO request ok"},
        {"RevisionName_s": "myapi--v2", "Log_s": "ERROR timeout"},
        {"RevisionName_s": "myapi--v2", "Log_s": "ERROR upstream"},
    ]
