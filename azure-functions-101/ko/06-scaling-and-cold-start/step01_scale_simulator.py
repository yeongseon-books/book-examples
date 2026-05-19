from __future__ import annotations


def estimate_instances(requests_per_second: int, concurrency_per_instance: int) -> int:
    return max(1, (requests_per_second + concurrency_per_instance - 1) // concurrency_per_instance)


def cold_start_risk(always_ready: int) -> str:
    return "low" if always_ready >= 1 else "high"


def run() -> dict[str, int | str]:
    return {"instances": estimate_instances(250, 50), "cold_start_risk": cold_start_risk(0)}


if __name__ == "__main__":
    print(run())
