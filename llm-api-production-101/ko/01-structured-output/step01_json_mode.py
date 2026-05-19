"""Llm Api Production 101 - Episode 1: Json mode."""

import json
import os

from groq import Groq


def call_json_mode(client: Groq, prompt: str) -> dict:
    """Call json mode."""
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "당신은 데이터 추출 도우미입니다. 항상 올바른 JSON만 반환하세요.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.1,
    )
    raw = completion.choices[0].message.content or "{}"
    return json.loads(raw)


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    result = call_json_mode(
        client,
        "상품명=노트북, 가격=1500000, 재고=true 정보를 JSON으로 추출해 주세요.",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    assert isinstance(result, dict), "응답이 dict가 아닙니다."
    print("JSON 모드 파싱에 성공했습니다.")


if __name__ == "__main__":
    main()
