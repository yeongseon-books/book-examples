"""Simulate base model vs fine-tuned behavior with Groq API"""

from __future__ import annotations

import os
from textwrap import indent
from typing import Any

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def request_completion(client: Any, system_prompt: str, user_prompt: str) -> str:
    """Request completion."""
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def main() -> None:
    """Main."""
    if Groq is None:
        print(
            "The groq package is missing. Install it with `pip install groq==1.2.0` and run again."
        )
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY environment variable is missing.")
        return

    client = Groq(api_key=api_key)
    user_request = "Write a four-sentence incident update for our SaaS analytics product. Include root cause, impact scope, mitigation status, and the next update time."

    print(
        "Running the same user request with a base prompt and a domain-specific prompt."
    )
    print()
    print("User request")
    print(indent(user_request, prefix="  "))
    print()

    base_response = request_completion(
        client,
        "You are a general-purpose assistant. Respond clearly, briefly, and without domain-specific style constraints.",
        user_request,
    )
    tuned_response = request_completion(
        client,
        "You are specialized in writing B2B SaaS incident updates for a product named PulseBoard. Use customer-facing language, mention current status, next update time, and confidence-building operational tone.",
        user_request,
    )

    print("Base-style response")
    print("-" * 80)
    print(base_response)
    print()
    print("Fine-tuned-style response")
    print("-" * 80)
    print(tuned_response)


if __name__ == "__main__":
    main()
