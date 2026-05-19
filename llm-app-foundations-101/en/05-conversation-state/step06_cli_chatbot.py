"""
Step 06 — Complete CLI chatbot
======================================================
Run:
    python step06_cli_chatbot.py

Combine an input loop, summary compression,
and token budget management into one practical CLI chatbot.
"""

import os
from typing import TypedDict

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam, ChatCompletionSystemMessageParam

MODEL = "llama-3.1-8b-instant"
MAX_INPUT_TOKENS = 6000
RAW_TURN_LIMIT = 6


class ChatState(TypedDict):
    """Chat state."""

    summary_text: str
    recent_turns: list[ChatCompletionMessageParam]


def message_text(message: ChatCompletionMessageParam) -> str:
    """Message text."""
    content = message.get("content")
    if isinstance(content, str):
        return content
    return ""


def rough_token_count(messages: list[ChatCompletionMessageParam]) -> int:
    """Rough token count."""
    total_chars = sum(len(message_text(message)) for message in messages)
    return (total_chars // 4) + len(messages) * 12


def summarize_old_turns(
    client: Groq,
    old_turns: list[ChatCompletionMessageParam],
    current_summary: str,
) -> str:
    """Summarize old turns."""
    prompt: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": (
                "Compress the conversation history. "
                "Keep the user's goal, confirmed facts, preferences, and unresolved questions."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Current summary:\n{current_summary or '(none)'}\n\n"
                f"Conversation to add:\n{old_turns}"
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
    """Build messages."""
    messages: list[ChatCompletionMessageParam] = [system_message]
    if summary_text:
        messages.append(
            {
                "role": "system",
                "content": f"Previous conversation summary:\n{summary_text}",
            }
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
    """Compress if needed."""
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
        raise ValueError("The input is too long. Start a new session with /reset.")


def ask(
    client: Groq,
    system_message: ChatCompletionSystemMessageParam,
    state: ChatState,
    user_text: str,
) -> str:
    """Ask."""
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
        raise RuntimeError("Did not receive usage metadata.")
    print(f"[tokens] prompt={usage.prompt_tokens} total={usage.total_tokens}")
    return answer


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": (
            "You are a practical Python and LLM app assistant. "
            "Say when you do not know something, and keep answers short and accurate."
        ),
    }
    state: ChatState = {"summary_text": "", "recent_turns": []}

    print("Starting the multi-turn chatbot. Commands: /reset, /summary, /quit")

    while True:
        user_text = input("\nyou> ").strip()

        if not user_text:
            continue
        if user_text == "/quit":
            break
        if user_text == "/reset":
            state = {"summary_text": "", "recent_turns": []}
            print("assistant> Session reset.")
            continue
        if user_text == "/summary":
            print(f"assistant> Current summary:\n{state['summary_text'] or '(none)'}")
            continue

        try:
            print(f"assistant> {ask(client, system_message, state, user_text)}")
        except ValueError as exc:
            print(f"assistant> {exc}")


if __name__ == "__main__":
    main()
