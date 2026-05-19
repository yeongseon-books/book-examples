"""Llm Apps Ops 101 - Episode 2: Cost tracking."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

from en.common import (
    DEFAULT_INPUT_RATE,
    DEFAULT_OUTPUT_RATE,
    build_logger,
    estimate_tokens,
)

logger = build_logger("en.cost")


@dataclass(slots=True)
class PricingTable:
    """Pricing table."""

    input_rate_per_million: float = DEFAULT_INPUT_RATE
    output_rate_per_million: float = DEFAULT_OUTPUT_RATE

    def calculate(self, *, input_tokens: int, output_tokens: int) -> float:
        """Calculate."""
        input_cost = (input_tokens / 1_000_000) * self.input_rate_per_million
        output_cost = (output_tokens / 1_000_000) * self.output_rate_per_million
        return round(input_cost + output_cost, 8)


@dataclass(slots=True)
class CostRecord:
    """Cost record."""

    feature: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    ts: float = field(default_factory=time.time)


class CostTracker:
    """Cost tracker."""

    def __init__(self, pricing: PricingTable) -> None:
        self.pricing = pricing
        self.records: list[CostRecord] = []

    def track(self, feature: str, prompt: str, response: str) -> CostRecord:
        """Track."""
        input_tokens = estimate_tokens(prompt)
        output_tokens = estimate_tokens(response)
        cost_usd = self.pricing.calculate(
            input_tokens=input_tokens, output_tokens=output_tokens
        )
        record = CostRecord(
            feature=feature,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost_usd,
        )
        self.records.append(record)
        logger.info(
            "Tracked cost event.",
            extra={
                "payload": {
                    "feature": feature,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "cost_usd": cost_usd,
                }
            },
        )
        return record

    def summary(self) -> dict[str, Any]:
        """Summary."""
        total_cost = round(sum(item.cost_usd for item in self.records), 8)
        total_tokens = sum(
            item.input_tokens + item.output_tokens for item in self.records
        )
        return {
            "requests": len(self.records),
            "total_tokens": total_tokens,
            "total_cost_usd": total_cost,
        }


class TTLCache:
    """TTL cache."""

    def __init__(self, ttl_seconds: int = 30) -> None:
        self.ttl_seconds = ttl_seconds
        self._store: dict[str, tuple[float, str]] = {}

    def get(self, key: str) -> str | None:
        """Get."""
        item = self._store.get(key)
        if item is None:
            return None
        expires_at, value = item
        if time.time() >= expires_at:
            self._store.pop(key, None)
            logger.info("TTL cache entry expired.", extra={"payload": {"key": key}})
            return None
        return value

    def set(self, key: str, value: str) -> None:
        """Set."""
        self._store[key] = (time.time() + self.ttl_seconds, value)
        logger.info(
            "Stored response in TTL cache.",
            extra={"payload": {"key": key, "ttl_seconds": self.ttl_seconds}},
        )


def demo() -> None:
    """Demo."""
    tracker = CostTracker(PricingTable())
    cache = TTLCache(ttl_seconds=10)
    prompt = "Summarize this week's incident review in three sentences."
    response = "This week's outage combined rising cache misses with database latency."
    tracker.track("incident-summary", prompt, response)
    cache.set(prompt, response)
    print(tracker.summary())
    print(cache.get(prompt))


if __name__ == "__main__":
    demo()
