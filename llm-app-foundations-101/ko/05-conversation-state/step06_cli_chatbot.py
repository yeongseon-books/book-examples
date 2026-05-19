"""
Step 06 — 완성 CLI 챗봇
======================================================
실행:
    python step06_cli_chatbot.py

입력 루프, 요약 압축, 토큰 예산 관리를 하나로 합친
실용적인 CLI 챗봇 예제입니다.
"""

import os
from typing import TypedDict

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam, ChatCompletionSystemMessageParam

MODEL = "llama-3.1-8b-instant"
MAX_INPUT_TOKENS = 6000
RAW_TURN_LIMIT = 6


class ChatState(TypedDict):
    summary_text: str
    recent_turns: list[ChatCompletionMessageParam]


def message_text(message: ChatCompletionMessageParam) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return content
    return ""


def rough_token_count(messages: list[ChatCompletionMessageParam]) -> int:
    total_chars = sum(len(message_text(message)) for message in messages)
    return (total_chars // 4) + len(messages) * 12


def summarize_old_turns(
    client: Groq,
    old_turns: list[ChatCompletionMessageParam],
    current_summary: str,
) -> str:
    prompt: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": (
                "대화 이력을 압축 요약하세요. "
                "반드시 사용자 목표, 확정된 사실, 선호, 미해결 질문을 남기세요."
            ),
        },
        {
            "role": "user",
            "content": (
                f"기존 요약:\n{current_summary or '(없음)'}\n\n"
                f"추가할 대화:\n{old_turns}"
            ),
        },
    ]
    completion = client.chat.completions.create(
        model=MODEL,
        temperature=0.1,
        messages=prompt,
    )
    return completion.choices[0].message.content or current_summary


def build_messages(
    system_message: ChatCompletionSystemMessageParam,
    summary_text: str,
    recent_turns: list[ChatCompletionMessageParam],
    user_text: str,
) -> list[ChatCompletionMessageParam]:
    messages: list[ChatCompletionMessageParam] = [system_message]
    if summary_text:
        messages.append(
            {"role": "system", "content": f"이전 대화 요약:\n{summary_text}"}
        )
    messages.extend(recent_turns)
    messages.append({"role": "user", "content": user_text})
    return messages


def compress_if_needed(
    client: Groq,
    system_message: ChatCompletionSystemMessageParam,
    next_user_text: str,
    state: ChatState,
) -> None:
    summary_text = state["summary_text"]
    recent_turns = state["recent_turns"]
    messages = build_messages(
        system_message, summary_text, recent_turns, next_user_text
    )
    if rough_token_count(messages) <= MAX_INPUT_TOKENS:
        return

    if len(recent_turns) > RAW_TURN_LIMIT:
        old_turns = recent_turns[:-RAW_TURN_LIMIT]
        state["recent_turns"] = recent_turns[-RAW_TURN_LIMIT:]
        state["summary_text"] = summarize_old_turns(client, old_turns, summary_text)
        summary_text = state["summary_text"]
        recent_turns = state["recent_turns"]

    messages = build_messages(
        system_message, summary_text, recent_turns, next_user_text
    )
    if rough_token_count(messages) > MAX_INPUT_TOKENS:
        raise ValueError("입력이 너무 깁니다. /reset으로 새 세션을 시작하세요.")


def ask(
    client: Groq,
    system_message: ChatCompletionSystemMessageParam,
    state: ChatState,
    user_text: str,
) -> str:
    compress_if_needed(client, system_message, user_text, state)
    messages = build_messages(
        system_message, state["summary_text"], state["recent_turns"], user_text
    )
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.3,
    )

    answer = completion.choices[0].message.content or ""
    state["recent_turns"].append({"role": "user", "content": user_text})
    state["recent_turns"].append({"role": "assistant", "content": answer})

    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")
    print(f"[tokens] prompt={usage.prompt_tokens} total={usage.total_tokens}")
    return answer


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": (
            "당신은 실무형 파이썬 및 LLM 앱 도우미입니다. "
            "모르면 모른다고 말하고, 답변은 짧고 정확하게 유지하세요."
        ),
    }
    state: ChatState = {"summary_text": "", "recent_turns": []}

    print("멀티턴 챗봇을 시작합니다. /reset, /summary, /quit 명령을 지원합니다.")

    while True:
        user_text = input("\n사용자> ").strip()

        if not user_text:
            continue
        if user_text == "/quit":
            break
        if user_text == "/reset":
            state = {"summary_text": "", "recent_turns": []}
            print("도우미> 세션을 초기화했습니다.")
            continue
        if user_text == "/summary":
            print(f"도우미> 현재 요약:\n{state['summary_text'] or '(없음)'}")
            continue

        try:
            print(f"도우미> {ask(client, system_message, state, user_text)}")
        except ValueError as exc:
            print(f"도우미> {exc}")


if __name__ == "__main__":
    main()
