"""Llm Api Production 101 - Episode 2: Tool loop."""

import json
import os
from typing import Any, cast

from groq import Groq

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_product",
            "description": "Search the product catalog by name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "max_results": {"type": "integer", "default": 3},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_to_cart",
            "description": "Add a product to the cart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "string"},
                    "quantity": {"type": "integer"},
                },
                "required": ["product_id", "quantity"],
            },
        },
    },
]

CATALOG = {
    "laptop": {"id": "P001", "price": 1500000},
    "mouse": {"id": "P002", "price": 35000},
    "keyboard": {"id": "P003", "price": 89000},
}

CART: list[dict] = []


def search_product(query: str, max_results: int = 3) -> list[dict]:
    """Search product."""
    return [
        {"id": value["id"], "name": name, "price": value["price"]}
        for name, value in CATALOG.items()
        if query.lower() in name.lower()
    ][:max_results]


def add_to_cart(product_id: str, quantity: int) -> dict:
    """Add to cart."""
    CART.append({"product_id": product_id, "quantity": quantity})
    return {"status": "added", "product_id": product_id, "quantity": quantity}


def dispatch(name: str, args: dict):
    """Dispatch."""
    if name == "search_product":
        return search_product(**args)
    if name == "add_to_cart":
        return add_to_cart(**args)
    raise ValueError(f"Unknown tool: {name}")


def run_loop(client: Groq, user_message: str) -> str:
    """Run loop."""
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_message}]

    while True:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=cast("Any", messages),
            tools=cast("Any", TOOLS),
            tool_choice="auto",
        )
        choice = response.choices[0]
        msg = choice.message

        assistant_entry = {"role": "assistant", "content": msg.content}
        if msg.tool_calls:
            assistant_entry["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in msg.tool_calls
            ]
        messages.append(assistant_entry)

        if choice.finish_reason != "tool_calls":
            return choice.message.content or ""

        for tc in msg.tool_calls or []:
            args = json.loads(tc.function.arguments)
            result = dispatch(tc.function.name, args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result, ensure_ascii=False),
                }
            )


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    answer = run_loop(client, "Add two mouse items to my cart.")
    print(answer)
    print(f"cart: {CART}")


if __name__ == "__main__":
    main()


# Expected output:
# Step 1: Tool call → get_weather({"location": "NYC"})
# Step 1: Result → {"temperature": 45, "condition": "cloudy"}
# Step 2: Tool call → get_forecast({"location": "NYC", "days": 3})
# Step 2: Result → {"forecast": ["rain", "clear", "clear"]}
# Final: It's currently 45°F and cloudy in NYC. The 3-day forecast...
