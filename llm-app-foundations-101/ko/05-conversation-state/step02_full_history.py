\
"""
Step 02 — 전체 이력 누적 패턴
======================================================
실행:
    python step02_full_history.py

history 리스트에 모든 user와 assistant 턴을 누적해
멀티턴 대화 맥락을 이어가는 가장 단순한 패턴입니다.
"""
import os
from typing import Any

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam


def ask(client: Groq, history: list[ChatCompletionMessageParam], user_text: str) -> str:
    history.append({"role": "user", "content": user_text})

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history,
        temperature=0.2,
    )

    answer = completion.choices[0].message.content or ""
    history.append({"role": "assistant", "content": answer})

    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")
    print(f"[tokens] prompt={usage.prompt_tokens} total={usage.total_tokens}")
    return answer


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    history: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": "당신은 간결한 기술 지원 도우미입니다.",
        }
    ]
    turns = [
        "내 서비스는 월 구독형 SaaS야. 기억해 줘.",
        "그럼 환불 정책 문구를 한 줄로 써 줘.",
        "좀 더 고객 친화적인 톤으로 다시 써 줘.",
    ]

    for user_text in turns:
        print(f"\n사용자> {user_text}")
        print(f"도우미> {ask(client, history, user_text)}")


if __name__ == "__main__":
    main()
