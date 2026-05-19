"""Ai Web Dev 101 - Episode 1: Tool agent."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLM, get_exchange_rate, get_weather, safe_calculate


def run_agent(goal: str, max_steps: int = 5) -> dict[str, object]:
    """Run agent."""
    llm = MockLLM()
    traces: list[str] = []
    result: str = ""
    for idx, call in enumerate(llm.plan_tools(goal), start=1):
        if idx > max_steps:
            break
        if call.name == "get_weather":
            weather = get_weather(str(call.args["location"]))
            traces.append(f"weather={weather['condition']}")
        elif call.name == "get_exchange_rate":
            rate = get_exchange_rate(
                str(call.args["from_currency"]), str(call.args["to_currency"])
            )
            traces.append(f"rate={rate['rate']}")
        elif call.name == "calculate":
            calc = safe_calculate(str(call.args["expression"]))
            traces.append(f"calc={calc}")
            result = f"최종 금액은 {int(calc)}원입니다."
    if not result:
        result = "도구 실행이 필요하지 않은 요청입니다."
    return {"result": result, "traces": traces, "steps": len(traces)}
