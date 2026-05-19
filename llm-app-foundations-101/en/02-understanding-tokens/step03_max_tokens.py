"""
Step 03 — Control output length with max_tokens
======================================================
Run:
    python step03_max_tokens.py

Intentionally truncate a response with a small max_tokens value,
then inspect completion_tokens and finish_reason.
"""

import os

from groq import Groq


def call_with_max_tokens(client: Groq, max_tokens: int) -> None:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Explain the difference between Python generators and lists in detail with an example.",
            }
        ],
        max_tokens=max_tokens,
    )
    usage = completion.usage
    if usage is None:
        raise RuntimeError("Did not receive usage metadata.")

    print(f"\n=== max_tokens={max_tokens} ===")
    print(completion.choices[0].message.content)
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"finish_reason={completion.choices[0].finish_reason}")

    if completion.choices[0].finish_reason == "length":
        print("Warning: the output hit the length limit and stopped early.")


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    call_with_max_tokens(client, max_tokens=40)
    call_with_max_tokens(client, max_tokens=300)


if __name__ == "__main__":
    main()
