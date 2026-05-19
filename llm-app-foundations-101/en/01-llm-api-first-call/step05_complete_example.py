"""
Step 05 — Complete example
======================================================
Run:
    python step05_complete_example.py

Combine the core ideas of lesson 01 in one file:
system message, user message, answer text, and usage metadata.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a concise Python tutor.",
            },
            {
                "role": "user",
                "content": (
                    "Explain the difference between a function and a method to a Python beginner in no more than five sentences, "
                    "and add one short example line."
                ),
            },
        ],
    )

    content = completion.choices[0].message.content or ""
    usage = completion.usage
    if usage is None:
        raise RuntimeError("Did not receive usage metadata.")

    print("=== answer ===")
    print(content)
    print()
    print("=== metadata ===")
    print(f"model: {completion.model}")
    print(f"finish_reason: {completion.choices[0].finish_reason}")
    print(f"prompt_tokens: {usage.prompt_tokens}")
    print(f"completion_tokens: {usage.completion_tokens}")
    print(f"total_tokens: {usage.total_tokens}")


if __name__ == "__main__":
    main()
