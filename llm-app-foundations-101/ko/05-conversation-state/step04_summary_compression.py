"""
Step 04 — 요약 기반 압축 패턴
======================================================
실행:
    python step04_summary_compression.py

오래된 대화 이력을 LLM으로 요약해 summary_text에 보존하고
최근 raw 턴만 원문으로 유지하는 압축 패턴입니다.
"""

import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam, ChatCompletionSystemMessageParam


def summarize_history(
    client: Groq,
    history_chunk: list[ChatCompletionMessageParam],
    current_summary: str,
) -> str:
    """Summarize history."""
    prompt: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": (
                "다음 대화 이력을 짧게 압축하세요. "
                "반드시 사용자 목표, 확정된 사실, 미해결 항목을 유지하세요."
            ),
        },
        {
            "role": "user",
            "content": (
                f"기존 요약:\n{current_summary or '(없음)'}\n\n"
                f"새로 압축할 대화:\n{history_chunk}"
            ),
        },
    ]
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=prompt,
        temperature=0.1,
    )
    return completion.choices[0].message.content or current_summary


def build_messages(
    system_message: ChatCompletionSystemMessageParam,
    summary_text: str,
    recent_turns: list[ChatCompletionMessageParam],
    user_text: str,
) -> list[ChatCompletionMessageParam]:
    """Build messages."""
    messages: list[ChatCompletionMessageParam] = [system_message]
    if summary_text:
        messages.append(
            {"role": "system", "content": f"이전 대화 요약:\n{summary_text}"}
        )
    messages.extend(recent_turns)
    messages.append({"role": "user", "content": user_text})
    return messages


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": "당신은 프로젝트 관리 챗봇입니다.",
    }
    summary_text = ""
    recent_turns: list[ChatCompletionMessageParam] = []
    turns = [
        "우리 프로젝트 이름은 AcmeCloud야.",
        "주요 기능은 파일 업로드와 공유야.",
        "출시 목표는 다음 달 말이야.",
        "지금까지 정리한 내용을 한 번 요약해 줘.",
    ]

    for user_text in turns:
        messages = build_messages(system_message, summary_text, recent_turns, user_text)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.3,
        )
        answer = completion.choices[0].message.content or ""
        recent_turns.append({"role": "user", "content": user_text})
        recent_turns.append({"role": "assistant", "content": answer})

        print(f"사용자> {user_text}")
        print(f"도우미> {answer}\n")

    print("=== 이력 압축 실행 ===")
    summary_text = summarize_history(client, recent_turns, summary_text)
    recent_turns.clear()
    print(f"summary:\n{summary_text}")


if __name__ == "__main__":
    main()
