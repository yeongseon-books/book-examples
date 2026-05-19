from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ToolCall:
    name: str
    args: dict[str, str]


class MockLLM:
    def chat(
        self, system: str, user: str, temperature: float = 0.2, max_tokens: int = 200
    ) -> dict[str, object]:
        tone = "정확" if temperature <= 0.3 else "창의"
        content = f"[{tone}] {system[:20]} | {user[:40]}"
        usage = {
            "prompt_tokens": len((system + user).split()),
            "completion_tokens": min(max_tokens, max(8, len(content.split()))),
        }
        usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
        return {
            "choices": [{"message": {"role": "assistant", "content": content}}],
            "usage": usage,
        }

    def plan_tools(self, goal: str) -> list[ToolCall]:
        g = goal.lower()
        calls: list[ToolCall] = []
        if "환율" in g or "달러" in g:
            calls.append(
                ToolCall(
                    "get_exchange_rate", {"from_currency": "USD", "to_currency": "KRW"}
                )
            )
        if "날씨" in g:
            calls.append(ToolCall("get_weather", {"location": "서울"}))
        if "수수료" in g:
            calls.append(ToolCall("calculate", {"expression": "100*1350*0.9"}))
        return calls


def get_weather(location: str) -> dict[str, str]:
    data = {
        "서울": {"location": "서울", "temperature": "25도", "condition": "맑음"},
        "부산": {"location": "부산", "temperature": "22도", "condition": "구름"},
    }
    return data.get(
        location,
        {"location": location, "temperature": "알 수 없음", "condition": "정보 없음"},
    )


def get_exchange_rate(from_currency: str, to_currency: str) -> dict[str, object]:
    rates = {"USD_KRW": 1350}
    pair = f"{from_currency}_{to_currency}"
    return {"pair": pair, "rate": rates.get(pair, 1300)}


def safe_calculate(expression: str) -> float:
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError("unsafe expression")
    return float(eval(expression, {"__builtins__": {}}, {}))
