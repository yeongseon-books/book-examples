import json
import os

from groq import Groq

SCHEMA_INSTRUCTION = """
다음 스키마에 정확히 맞는 JSON으로만 응답하세요:
{
  "category": "billing" | "technical" | "account",
  "priority": "low" | "medium" | "high",
  "summary": "<한 문장 요약>"
}
"""


def classify_ticket(client: Groq, ticket: str) -> dict:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SCHEMA_INSTRUCTION},
            {"role": "user", "content": ticket},
        ],
        response_format={"type": "json_object"},
        temperature=0.0,
    )
    return json.loads(completion.choices[0].message.content or "{}")


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    tickets = [
        "이번 달 청구 금액이 지난달보다 두 배 이상 높습니다.",
        "CSV 업로드 버튼을 누르면 500 오류가 발생합니다.",
        "비밀번호를 바꾼 뒤에도 로그인이 되지 않습니다.",
    ]

    for ticket in tickets:
        result = classify_ticket(client, ticket)
        print(f"티켓: {ticket}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print()

        assert result.get("category") in {"billing", "technical", "account"}
        assert result.get("priority") in {"low", "medium", "high"}
        assert isinstance(result.get("summary"), str)

    print("스키마 검증을 통과했습니다.")


if __name__ == "__main__":
    main()
