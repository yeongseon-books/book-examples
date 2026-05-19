"""
Step 01 — Compare answers with and without a system message
======================================================
Run:
    python step01_system_effect.py

Send the same question with and without a system message
to compare how the response style changes.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    question = "Explain the difference between a Python dictionary and a list."

    without_system = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question}],
        temperature=0.2,
    )

    with_system = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a technical tutor for Python beginners. "
                    "Always answer in English, start with one short paragraph, "
                    "and end with three bullet points that summarize the core differences. "
                    "Do not guess, and keep the explanation beginner-friendly."
                ),
            },
            {"role": "user", "content": question},
        ],
        temperature=0.2,
    )

    print("[without system]")
    print(without_system.choices[0].message.content)
    print()
    print("[with system]")
    print(with_system.choices[0].message.content)


if __name__ == "__main__":
    main()


# Expected output:
# [No system prompt] Sure, here's a joke: Why did the programmer quit?
# [With system prompt] Arr matey! Why did the pirate learn Python?
# Because he wanted to master the C!
