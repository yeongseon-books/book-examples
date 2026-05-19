"""
Step 03 — sliding window 패턴
======================================================
실행:
    python step03_sliding_window.py

최근 세 턴만 유지해 토큰 예산을 고정하는
sliding window 패턴입니다.
"""

import os
from collections import deque

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam, ChatCompletionSystemMessageParam


def ask(
    client: Groq,
    system_message: ChatCompletionSystemMessageParam,
    recent_turns: deque[ChatCompletionMessageParam],
    user_text: str,
) -> str:
    """Ask."""
    recent_turns.append({"role": "user", "content": user_text})

    messages: list[ChatCompletionMessageParam] = [system_message, *recent_turns]
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.3,
    )

    answer = completion.choices[0].message.content or ""
    recent_turns.append({"role": "assistant", "content": answer})

    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")
    print(f"[tokens] prompt={usage.prompt_tokens} window_size={len(recent_turns)}")
    return answer


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": "당신은 파이썬 학습을 돕는 챗봇입니다.",
    }
    recent_turns: deque[ChatCompletionMessageParam] = deque(maxlen=6)
    turns = [
        "리스트와 튜플의 차이를 설명해 줘.",
        "방금 말한 튜플에 예시 코드도 보여줘.",
        "딕셔너리는 어떤 경우에 써?",
        "집합은 뭐가 달라?",
        "지금까지 설명한 자료형 중 가장 자주 쓰는 건 뭐야?",
    ]

    for user_text in turns:
        print(f"\n사용자> {user_text}")
        print(f"도우미> {ask(client, system_message, recent_turns, user_text)}")


if __name__ == "__main__":
    main()
