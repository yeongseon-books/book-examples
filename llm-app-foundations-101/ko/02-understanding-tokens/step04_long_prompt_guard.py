\
"""
Step 04 — 긴 프롬프트와 finish_reason 감지
======================================================
실행:
    python step04_long_prompt_guard.py

tiktoken으로 사전 추정한 뒤 API를 호출하고,
usage 비교와 finish_reason 확인까지 한 흐름으로 보여줍니다.
"""
import os

import tiktoken
from groq import Groq


def estimate_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    long_text = " ".join(
        ["파이썬 웹 애플리케이션에서 요청 로그와 예외 로그를 함께 남기는 이유를 설명해 주세요."] * 200
    )
    instruction = "다음 문장을 읽고 핵심만 열 개의 불릿으로 정리해 주세요."
    user_content = instruction + "\n\n" + long_text

    estimated = estimate_tokens(user_content)
    print(f"estimated_prompt_tokens={estimated}")

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_content}],
        max_tokens=60,
    )

    choice = completion.choices[0]
    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")

    print(choice.message.content)
    print()
    print(f"prompt_tokens={usage.prompt_tokens}")
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"total_tokens={usage.total_tokens}")
    print(f"finish_reason={choice.finish_reason}")

    if choice.finish_reason == "length":
        print("경고: 출력이 길이 제한에 걸려 중간에서 끝났습니다.")


if __name__ == "__main__":
    main()
