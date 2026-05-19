"""Llm Api Production 101 - Episode 3: Error handling."""

import json
import os

from groq import Groq


class SchemaError(Exception):
    """Schema error."""

    pass


SCHEMA_INSTRUCTION = """
Respond with JSON: {"name": string, "price": number, "in_stock": boolean}
"""


def extract_product(client: Groq, text: str) -> dict:
    """Extract product."""
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SCHEMA_INSTRUCTION},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
        temperature=0.0,
    )
    raw = completion.choices[0].message.content or ""

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SchemaError(f"Failed to parse JSON: {exc}; raw={raw!r}") from exc

    required = {"name", "price", "in_stock"}
    missing = required - data.keys()
    if missing:
        raise SchemaError(f"Missing required fields: {sorted(missing)}; data={data}")

    if not isinstance(data["price"], int | float):
        raise SchemaError(f"price must be numeric: {data['price']!r}")

    return data


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    cases = [
        "The product is a wireless mouse, the price is 35000, and it is in stock.",
        "mechanical keyboard 89000 out of stock",
    ]

    for case in cases:
        try:
            result = extract_product(client, case)
            print(f"Success: {result}")
        except SchemaError as exc:
            print(f"SchemaError: {exc}")


if __name__ == "__main__":
    main()
