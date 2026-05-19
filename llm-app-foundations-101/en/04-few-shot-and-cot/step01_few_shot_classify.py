"""
Step 01 — Basic few-shot classification
======================================================
Run:
    python step01_few_shot_classify.py

Use a system prompt and example pairs to classify a support ticket
into category, priority, and reason.
"""

import os
from typing import Any

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": (
                "You are an operations assistant that classifies customer tickets. "
                "Always answer in this format only:\n"
                "category: <billing|technical|account>\n"
                "priority: <low|medium|high>\n"
                "reason: <one sentence>"
            ),
        },
        {
            "role": "user",
            "content": "The payment went through, but I never received the receipt email.",
        },
        {
            "role": "assistant",
            "content": (
                "category: billing\n"
                "priority: medium\n"
                "reason: This is a billing issue because the payment proof email is missing after checkout."
            ),
        },
        {
            "role": "user",
            "content": "I changed my password, but I still cannot log in.",
        },
        {
            "role": "assistant",
            "content": (
                "category: account\n"
                "priority: high\n"
                "reason: Losing account access can block the user from using the service."
            ),
        },
        {"role": "user", "content": "The server crashes whenever I click CSV upload."},
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
