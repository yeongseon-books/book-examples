"""Azure Functions 101 - Episode 1: Monitoring queries."""

from __future__ import annotations


def failure_rate(total: int, failed: int) -> float:
    """Failure rate."""
    if total == 0:
        return 0.0
    return round((failed / total) * 100.0, 2)


def kql_requests_last_hour() -> str:
    """Kql requests last hour."""
    return "requests | where timestamp > ago(1h) | summarize Total=count(), Failed=countif(success == false)"


def run() -> dict[str, float | str]:
    """Run."""
    return {"failure_rate": failure_rate(1000, 32), "kql": kql_requests_last_hour()}


if __name__ == "__main__":
    print(run())
