"""
Step 06 — Few-shot CoT policy decision
======================================================
Run:
    python step06_policy_decision.py

Apply a refund policy with a few-shot reasoning pattern
that outputs policy_check, decision, and reason.
"""

import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam

POLICY = (
    "Refund policy:\n"
    "- Full refund if it is within 7 days of payment and watch progress is under 20%\n"
    "- No refund if it is within 7 days of payment and watch progress is 20% or more\n"
    "- No refund after 7 days regardless of watch progress"
)


def build_messages(case: str) -> list[ChatCompletionMessageParam]:
    return [
        {
            "role": "system",
            "content": (
                "You are a refund review assistant for an online course service. "
                "Always answer with 1) policy_check 2) decision 3) reason."
            ),
        },
        {"role": "user", "content": POLICY},
        {
            "role": "user",
            "content": "It has been 3 days since payment, and the watch progress is 10%. Decide whether a refund is allowed.",
        },
        {
            "role": "assistant",
            "content": (
                "policy_check:\n"
                "1) It is within 7 days of payment.\n"
                "2) The watch progress is under 20%.\n"
                "decision: approved\n"
                "reason: The case satisfies both the time and watch-progress conditions for a full refund."
            ),
        },
        {
            "role": "user",
            "content": "It has been 5 days since payment, and the watch progress is 35%. Decide whether a refund is allowed.",
        },
        {
            "role": "assistant",
            "content": (
                "policy_check:\n"
                "1) It is within 7 days of payment.\n"
                "2) The watch progress is 20% or more.\n"
                "decision: denied\n"
                "reason: The time condition passes, but the watch-progress threshold blocks the refund."
            ),
        },
        {"role": "user", "content": case},
    ]


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    cases = [
        "It has been 10 days since payment, and the watch progress is 0%. Decide whether a refund is allowed.",
        "It has been 2 days since payment, and the watch progress is 5%. Decide whether a refund is allowed.",
    ]

    for case in cases:
        print(f"[case] {case}")
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=build_messages(case),
            temperature=0.0,
        )
        print(completion.choices[0].message.content)
        print()


if __name__ == "__main__":
    main()
