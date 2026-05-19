import json
import os
from typing import Any, cast

from groq import Groq


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_product",
            "description": "이름으로 상품 카탈로그를 검색합니다.",
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
            "description": "상품을 장바구니에 담습니다.",
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
    "노트북": {"id": "P001", "price": 1500000},
    "마우스": {"id": "P002", "price": 35000},
    "키보드": {"id": "P003", "price": 89000},
}

CART: list[dict] = []


def search_product(query: str, max_results: int = 3) -> list[dict]:
    return [
        {"id": value["id"], "name": name, "price": value["price"]}
        for name, value in CATALOG.items()
        if query.lower() in name.lower()
    ][:max_results]


def add_to_cart(product_id: str, quantity: int) -> dict:
    CART.append({"product_id": product_id, "quantity": quantity})
    return {"status": "added", "product_id": product_id, "quantity": quantity}


def dispatch(name: str, args: dict):
    if name == "search_product":
        return search_product(**args)
    if name == "add_to_cart":
        return add_to_cart(**args)
    raise ValueError(f"알 수 없는 도구입니다: {name}")


def run_loop(client: Groq, user_message: str) -> str:
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_message}]

    while True:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=cast(Any, messages),
            tools=cast(Any, TOOLS),
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
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    answer = run_loop(client, "마우스를 2개 장바구니에 담아 주세요.")
    print(answer)
    print(f"장바구니: {CART}")


if __name__ == "__main__":
    main()
