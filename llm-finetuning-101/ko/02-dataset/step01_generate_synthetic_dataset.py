"""Groq으로 합성 instruction-response 데이터 생성"""

from __future__ import annotations

import json
import os
from pathlib import Path

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
OUTPUT_PATH = Path(__file__).resolve().parent / "outputs" / "synthetic_pairs.json"


def extract_json(text: str):
    """Extract json."""
    text = text.strip()
    if text.startswith("```"):
        lines = [line for line in text.splitlines() if not line.startswith("```")]
        text = "\n".join(lines).strip()
    return json.loads(text)


def main() -> None:
    """Main."""
    if Groq is None:
        print("groq 패키지가 없어 합성 데이터 생성을 건너뜁니다.")
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY 환경 변수가 없어 합성 데이터 생성을 건너뜁니다.")
        return

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.5,
        messages=[
            {
                "role": "system",
                "content": "당신은 데이터셋 작성 도우미입니다. 결과는 반드시 JSON 배열만 출력하세요.",
            },
            {
                "role": "user",
                "content": "고객 지원 챗봇 파인튜닝용 instruction-response 데이터 5개를 JSON 배열로 생성해 주세요. 각 항목은 instruction, response, category 필드를 가져야 합니다. 한국어로 작성하세요.",
            },
        ],
    )
    content = response.choices[0].message.content or "[]"
    items = extract_json(content)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"저장 완료: {OUTPUT_PATH}")
    print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
