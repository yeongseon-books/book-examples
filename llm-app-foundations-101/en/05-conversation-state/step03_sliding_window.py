"""
Step 03 — Sliding window pattern
======================================================
Run:
    python step03_sliding_window.py

Keep only the most recent three turns
to stabilize the prompt token budget.
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
        raise RuntimeError("Did not receive usage metadata.")
    print(f"[tokens] prompt={usage.prompt_tokens} window_size={len(recent_turns)}")
    return answer


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": "You are a chatbot that helps people learn Python.",
    }
    recent_turns: deque[ChatCompletionMessageParam] = deque(maxlen=6)
    turns = [
        "Explain the difference between a list and a tuple.",
        "Show a code example for the tuple you just mentioned.",
        "When should I use a dictionary?",
        "How is a set different?",
        "Which of the data structures you explained so far is used most often?",
    ]

    for user_text in turns:
        print(f"\nyou> {user_text}")
        print(f"assistant> {ask(client, system_message, recent_turns, user_text)}")


if __name__ == "__main__":
    main()
