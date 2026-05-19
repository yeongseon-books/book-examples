\
"""
Step 03 — 응답 구조 해부
======================================================
실행:
    python step03_inspect_response.py

응답 전체를 JSON으로 출력하고,
content / usage / model / finish_reason 필드를 읽습니다.
"""
import json
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "HTTP API와 SDK의 차이를 세 문장으로 설명해 주세요.",
            }
        ],
    )

    print("=== 원본 응답 ===")
    print(json.dumps(completion.to_dict(), indent=2, ensure_ascii=False))

    print("\n=== 핵심 필드 ===")
    text = completion.choices[0].message.content
    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")

    print(f"content: {text}")
    print(f"model: {completion.model}")
    print(f"finish_reason: {completion.choices[0].finish_reason}")
    print(f"prompt_tokens: {usage.prompt_tokens}")
    print(f"completion_tokens: {usage.completion_tokens}")
    print(f"total_tokens: {usage.total_tokens}")
    print(f"request_id: {completion.id}")


if __name__ == "__main__":
    main()
