from __future__ import annotations

import json

from common import DEFAULT_MODEL, as_messages, as_tools, build_client, print_section, response_text


def lookup_order_total(order_id: str) -> str:
    totals = {
        "ORD-300": "주문 ORD-300의 총 결제 금액은 48,000원입니다.",
    }
    if order_id not in totals:
        raise ValueError(f"알 수 없는 주문 번호입니다: {order_id}")
    return totals[order_id]


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_order_total",
            "description": "주문 번호로 결제 금액을 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string"},
                },
                "required": ["order_id"],
            },
        },
    }
]


def run_safe_agent() -> None:
    client = build_client()
    messages: list[dict] = [
        {"role": "system", "content": "도구 오류가 나면 원인을 설명하고 대체 입력을 요청하세요."},
        {"role": "user", "content": "ORD-999 주문 금액을 확인해 주세요."},
    ]

    first = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=as_messages(messages),
        tools=as_tools(TOOLS),
        tool_choice="auto",
        temperature=0,
    )
    first_message = first.choices[0].message
    tool_calls = first_message.tool_calls or []

    messages.append(
        {
            "role": "assistant",
            "content": response_text(first_message),
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in tool_calls
            ],
        }
    )

    for tool_call in tool_calls:
        arguments = json.loads(tool_call.function.arguments)
        try:
            result = lookup_order_total(arguments["order_id"])
        except ValueError as exc:
            result = f"도구 오류: {exc}. 올바른 주문 번호를 다시 요청하세요."
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )

    final = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0)
    print_section("복구 답변")
    print(response_text(final.choices[0].message))


if __name__ == "__main__":
    run_safe_agent()
