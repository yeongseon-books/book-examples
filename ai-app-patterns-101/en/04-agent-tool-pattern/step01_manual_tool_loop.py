"""Ai App Patterns 101 - Episode 1: Manual tool loop."""

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
    """Lookup shipping status."""
    statuses = {
        "ORD-100": "Order ORD-100 left the warehouse and is scheduled to arrive tomorrow.",
        "ORD-200": "Order ORD-200 is still waiting for payment confirmation.",
    }
    return statuses.get(order_id, f"No shipping record was found for {order_id}.")


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_shipping_status",
            "description": "Look up the shipping status for an order id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "Order identifier"},
                },
                "required": ["order_id"],
            },
        },
    }
]


def run_agent() -> None:
    """Run agent."""
    client = build_client()
    messages: list[dict] = [
        {
            "role": "system",
            "content": "You are a customer support agent. Use tools when needed.",
        },
        {
            "role": "user",
            "content": "Please check the shipping status for order ORD-100.",
        },
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
    print_section("Final answer")
    print(response_text(final.choices[0].message))


if __name__ == "__main__":
    run_agent()
