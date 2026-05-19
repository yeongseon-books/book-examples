"""
Step 04 — Summary-based compression
======================================================
Run:
    python step04_summary_compression.py

Summarize older conversation turns with the LLM,
keep the summary in summary_text, and retain only recent raw turns.
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
                "Compress the following conversation history into a short summary. "
                "Always keep the user's goal, confirmed facts, and unresolved items."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Current summary:\n{current_summary or '(none)'}\n\n"
                f"New conversation to compress:\n{history_chunk}"
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
            {
                "role": "system",
                "content": f"Previous conversation summary:\n{summary_text}",
            }
        )
    messages.extend(recent_turns)
    messages.append({"role": "user", "content": user_text})
    return messages


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": "You are a project management chatbot.",
    }
    summary_text = ""
    recent_turns: list[ChatCompletionMessageParam] = []
    turns = [
        "Our project name is AcmeCloud.",
        "Its main features are file upload and sharing.",
        "The launch target is the end of next month.",
        "Please summarize what we have decided so far.",
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

        print(f"you> {user_text}")
        print(f"assistant> {answer}\n")

    print("=== run compression ===")
    summary_text = summarize_history(client, recent_turns, summary_text)
    recent_turns.clear()
    print(f"summary:\n{summary_text}")


if __name__ == "__main__":
    main()
