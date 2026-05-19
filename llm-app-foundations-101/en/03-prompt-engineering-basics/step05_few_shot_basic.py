"""
Step 05 — Put few-shot examples into the messages list
======================================================
Run:
    python step05_few_shot_basic.py

Place user and assistant examples before the final request
to demonstrate a target answer pattern.
"""

import os
from typing import Any

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": "You are a tutor who explains Python concepts with a one-line definition and a one-line analogy.",
        },
        {"role": "user", "content": "What is a class?"},
        {
            "role": "assistant",
            "content": (
                "Definition: A class is a blueprint for creating objects.\n"
                "Analogy: It is like a mold that stamps out pastries with the same shape."
            ),
        },
        {"role": "user", "content": "What is inheritance?"},
        {
            "role": "assistant",
            "content": (
                "Definition: Inheritance is a way to create a new class by reusing the properties and behavior of an existing one.\n"
                "Analogy: It is like copying a base template and adding only the parts you need."
            ),
        },
        {"role": "user", "content": "What is a decorator?"},
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
