from __future__ import annotations

import json

from common import (
    DEFAULT_MODEL,
    as_messages,
    as_tools,
    build_client,
    print_section,
    response_text,
)


def lookup_shipping_status(order_id: str) -> str:
    statuses = {
        "ORD-100": "주문 ORD-100은 물류센터에서 출고 완료되었고 내일 도착 예정입니다.",
        "ORD-200": "주문 ORD-200은 결제 확인 대기 상태입니다.",
    }
    return statuses.get(order_id, f"주문 {order_id} 정보가 없습니다.")


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_shipping_status",
            "description": "주문 번호로 배송 상태를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "주문 번호"},
                },
                "required": ["order_id"],
            },
        },
    }
]


def run_agent() -> None:
    client = build_client()
    messages: list[dict] = [
        {
            "role": "system",
            "content": "당신은 고객 지원 에이전트입니다. 필요한 경우 도구를 사용하세요.",
        },
        {"role": "user", "content": "ORD-100 주문 배송 상태를 알려 주세요."},
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
        result = lookup_shipping_status(arguments["order_id"])
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )

    final = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0
    )
    print_section("최종 답변")
    print(response_text(final.choices[0].message))


if __name__ == "__main__":
    run_agent()
