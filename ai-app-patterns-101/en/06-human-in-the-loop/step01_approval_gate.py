"""Ai App Patterns 101 - Episode 1: Approval gate."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

CASES = [
    {
        "request": "Approve an exception to the refund policy. The customer retried payment twice because of an outage.",
        "confidence": 0.91,
    },
    {
        "request": "Approve a penalty waiver for a VIP customer. There may be contractual risk.",
        "confidence": 0.42,
    },
]


def run_hitl_workflow() -> None:
    """Run hitl workflow."""
    client = build_client()

    for case in CASES:
        requires_human = case["confidence"] < 0.75
        decision = (
            "human approval required"
            if requires_human
            else "safe for automatic handling"
        )
        messages = [
            {
                "role": "system",
                "content": "Explain in English why the request should be auto-handled or sent to a human reviewer based on the confidence score.",
            },
            {
                "role": "user",
                "content": f"Request: {case['request']}\nConfidence: {case['confidence']}\nExpected path: {decision}",
            },
        ]
        response = client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.1
        )

        print_section(decision)
        print(case["request"])
        print(response_text(response.choices[0].message))


if __name__ == "__main__":
    run_hitl_workflow()
