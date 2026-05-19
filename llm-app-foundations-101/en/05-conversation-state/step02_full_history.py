"""
Step 02 — Keep the full conversation history
======================================================
Run:
    python step02_full_history.py

Accumulate every user and assistant turn in one history list
to preserve multi-turn context.
"""

import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam


def ask(client: Groq, history: list[ChatCompletionMessageParam], user_text: str) -> str:
    """Ask."""
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
        raise RuntimeError("Did not receive usage metadata.")
    print(f"[tokens] prompt={usage.prompt_tokens} total={usage.total_tokens}")
    return answer


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    history: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": "You are a concise technical support assistant.",
        }
    ]
    turns = [
        "My service is a monthly subscription SaaS. Please remember that.",
        "Now write a one-line refund policy message for it.",
        "Rewrite it in a more customer-friendly tone.",
    ]

    for user_text in turns:
        print(f"\nyou> {user_text}")
        print(f"assistant> {ask(client, history, user_text)}")


if __name__ == "__main__":
    main()
