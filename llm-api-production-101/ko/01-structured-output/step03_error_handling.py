"""Llm Api Production 101 - Episode 3: Error handling."""

import json
import os

from groq import Groq


class SchemaError(Exception):
    """Schema error."""

    pass


SCHEMA_INSTRUCTION = """
다음 JSON으로 응답하세요: {"name": string, "price": number, "in_stock": boolean}
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
        raise SchemaError(f"JSON 파싱에 실패했습니다: {exc}; raw={raw!r}") from exc

    required = {"name", "price", "in_stock"}
    missing = required - data.keys()
    if missing:
        raise SchemaError(f"필수 필드가 누락되었습니다: {sorted(missing)}; data={data}")

    if not isinstance(data["price"], int | float):
        raise SchemaError(f"price는 숫자여야 합니다: {data['price']!r}")

    return data


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    cases = [
        "상품명은 무선 마우스이고 가격은 35000원이며 재고가 있습니다.",
        "mechanical keyboard 89000 out of stock",
    ]

    for case in cases:
        try:
            result = extract_product(client, case)
            print(f"성공: {result}")
        except SchemaError as exc:
            print(f"SchemaError: {exc}")


if __name__ == "__main__":
    main()
