"""Shared utilities and domain models for Ai Agent 101."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone

Weather = dict[str, str | int]


def get_weather(city: str) -> Weather:
    """Get weather."""
    data: dict[str, Weather] = {
        "Seoul": {"temp": 22, "condition": "clear"},
        "Tokyo": {"temp": 18, "condition": "rain"},
        "Busan": {"temp": 20, "condition": "cloudy"},
    }
    return data.get(city, {"temp": 0, "condition": "unknown"})


def search_knowledge(query: str) -> list[dict[str, str]]:
    """Search knowledge."""
    corpus = [
        {"title": "FastAPI", "snippet": "FastAPI is async and type-driven."},
        {"title": "Flask", "snippet": "Flask is minimal and flexible."},
        {"title": "Agent", "snippet": "Observe, think, act, and check in a loop."},
    ]
    q = query.lower()
    return [
        item
        for item in corpus
        if q.split()[0] in item["title"].lower()
        or q.split()[0] in item["snippet"].lower()
    ] or corpus[:1]


def safe_calculate(expression: str) -> float:
    """Safe calculate."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError("unsafe expression")
    return float(eval(expression, {"__builtins__": {}}, {}))


def deterministic_score(text: str) -> float:
    """Deterministic score."""
    return round((sum(ord(ch) for ch in text) % 100) / 100, 2)


@dataclass
class ToolCall:
    """Tool call."""

    name: str
    args: dict[str, str]


class MockLLM:
    """Mock l l m."""

    def next_action(self, goal: str, state: dict[str, object]) -> ToolCall | str:
        """Next action."""
        g = goal.lower()
        if "weather" in g or "날씨" in g:
            city = "Tokyo" if "tokyo" in g or "도쿄" in g else "Seoul"
            if state.get("weather") is None:
                return ToolCall("get_weather", {"city": city})
            weather = state["weather"]
            if isinstance(weather, dict) and weather.get("condition") == "rain":
                return "Umbrella is recommended."
            return "Umbrella is not required."
        if "calculate" in g or "계산" in g:
            return ToolCall("calculate", {"expression": "1000*0.5"})
        return "Use search results to answer briefly."


def now_iso() -> str:
    """Now iso."""
    return datetime.now(timezone.utc).isoformat()


def retry(operation: Callable[[], object], max_attempts: int = 3) -> object:
    """Retry."""
    last_error: Exception | None = None
    for _ in range(max_attempts):
        try:
            return operation()
        except Exception as exc:  # noqa: PERF203
            last_error = exc
    if last_error is None:
        raise RuntimeError("retry failed")
    raise last_error
