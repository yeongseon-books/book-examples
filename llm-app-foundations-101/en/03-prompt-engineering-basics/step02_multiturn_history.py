"""
Step 02 — Build multi-turn history with assistant messages
======================================================
Run:
    python step02_multiturn_history.py

Add the first answer back into the messages list as an assistant turn,
then continue the conversation with the previous context.
"""

import os
from typing import Any

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": "You are a Python learning assistant. Keep answers short and accurate.",
        },
        {
            "role": "user",
            "content": "Explain the difference between a Python list and a tuple in one paragraph.",
        },
    ]

    first = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )
    assistant_text = first.choices[0].message.content or ""
    print("[turn 1]")
    print(assistant_text)
    print()

    messages.append({"role": "assistant", "content": assistant_text})
    messages.append(
        {
            "role": "user",
            "content": "Add a code example in no more than five lines.",
        }
    )

    second = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )
    print("[turn 2]")
    print(second.choices[0].message.content)


if __name__ == "__main__":
    main()
