\
"""
Step 03 — Compare weak examples and strong examples
======================================================
Run:
    python step03_example_quality.py

Attach weak examples and strong examples to the same target request
to show how example quality changes the result.
"""
import os
from typing import Any

from groq import Groq

SYSTEM_PROMPT = (
    "You classify SaaS customer tickets. "
    "Answer only in the format below:\n"
    "category: <billing|technical|account>\n"
    "priority: <low|medium|high>\n"
    "reason: <one sentence>"
)

TARGET = "I cannot log in because the password reset email never arrives."


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    bad_examples: list[Any] = [
        {"role": "user", "content": "The invoice amount looks wrong."},
        {
            "role": "assistant",
            "content": "This might be a billing problem or maybe an account problem. Ask the customer for more details first.",
        },
        {"role": "user", "content": "I cannot log in."},
        {
            "role": "assistant",
            "content": "The priority could be urgent or not. It depends on the situation.",
        },
    ]

    good_examples: list[Any] = [
        {"role": "user", "content": "It looks like my card was charged twice."},
        {
            "role": "assistant",
            "content": (
                "category: billing\n"
                "priority: high\n"
                "reason: Duplicate charges can cause direct financial harm and need quick attention."
            ),
        },
        {"role": "user", "content": "I get a 500 error when I click the profile photo upload button."},
        {
            "role": "assistant",
            "content": (
                "category: technical\n"
                "priority: medium\n"
                "reason: This is a feature failure, but it is not as immediately blocking as an account lockout."
            ),
        },
    ]

    bad_messages: list[Any] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Review the examples and classify the next ticket in the same format."},
        *bad_examples,
        {"role": "user", "content": TARGET},
    ]
    good_messages: list[Any] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *good_examples,
        {"role": "user", "content": TARGET},
    ]

    bad_run = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=bad_messages,
        temperature=0.2,
    )
    good_run = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=good_messages,
        temperature=0.2,
    )

    print("[bad examples]")
    print(bad_run.choices[0].message.content)
    print()
    print("[good examples]")
    print(good_run.choices[0].message.content)


if __name__ == "__main__":
    main()
