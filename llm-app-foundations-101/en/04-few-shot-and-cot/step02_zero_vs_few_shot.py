"""
Step 02 — Compare zero-shot and few-shot prompting
======================================================
Run:
    python step02_zero_vs_few_shot.py

Send the same ticket with zero-shot and few-shot prompts
to compare output format stability.
"""

import os

from groq import Groq

SYSTEM_PROMPT = (
    "You are an operations assistant that classifies SaaS support tickets. "
    "Always answer in this format only:\n"
    "category: <billing|technical|account>\n"
    "priority: <low|medium|high>\n"
    "reason: <one sentence>"
)

TICKET = (
    "We are on the team plan, but this month's bill is almost twice what we expected."
)


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    zero_shot = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": TICKET},
        ],
        temperature=0.2,
    )

    few_shot = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": "A refund still has not appeared on my card statement.",
            },
            {
                "role": "assistant",
                "content": (
                    "category: billing\n"
                    "priority: medium\n"
                    "reason: A delayed refund is a billing follow-up issue after payment."
                ),
            },
            {
                "role": "user",
                "content": "I receive the two-factor code, but the login still fails.",
            },
            {
                "role": "assistant",
                "content": (
                    "category: account\n"
                    "priority: high\n"
                    "reason: Losing account access can immediately block the user's work."
                ),
            },
            {"role": "user", "content": TICKET},
        ],
        temperature=0.2,
    )

    print("[zero-shot]")
    print(zero_shot.choices[0].message.content)
    print()
    print("[few-shot]")
    print(few_shot.choices[0].message.content)


if __name__ == "__main__":
    main()
