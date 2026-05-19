from __future__ import annotations

import json

from common import DEFAULT_MODEL, as_messages, as_tools, build_client, print_section, response_text


def lookup_order_total(order_id: str) -> str:
    totals = {
        "ORD-300": "The total amount for order ORD-300 is 48,000 KRW.",
    }
    if order_id not in totals:
        raise ValueError(f"Unknown order id: {order_id}")
    return totals[order_id]


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_order_total",
            "description": "Look up the total amount for an order.",
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
        {"role": "system", "content": "If a tool fails, explain the issue and ask for a corrected input."},
        {"role": "user", "content": "Please check the amount for order ORD-999."},
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
            result = f"Tool error: {exc}. Ask the user for a valid order id."
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )

    final = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0)
    print_section("Recovery answer")
    print(response_text(final.choices[0].message))


if __name__ == "__main__":
    run_safe_agent()
