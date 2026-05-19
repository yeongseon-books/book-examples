\
"""
Step 01 — usage 필드 읽기
======================================================
실행:
    python step01_read_usage.py

API 호출 후 usage.prompt_tokens / completion_tokens / total_tokens를
읽고 finish_reason을 함께 출력합니다.
"""
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "파이썬 데코레이터를 두 문단 이내로 설명해 주세요.",
            }
        ],
    )

    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")

    print(completion.choices[0].message.content)
    print()
    print(f"finish_reason={completion.choices[0].finish_reason}")
    print(f"prompt_tokens={usage.prompt_tokens}")
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"total_tokens={usage.total_tokens}")


if __name__ == "__main__":
    main()
