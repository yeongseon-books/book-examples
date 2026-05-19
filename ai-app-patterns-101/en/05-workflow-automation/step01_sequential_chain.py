"""Ai App Patterns 101 - Episode 1: Sequential chain."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

REQUEST = "The customer wants to keep price stable while shortening time to launch. Draft a proposal email for adopting AI document search."


def run_sequential_chain() -> None:
    """Run sequential chain."""
    client = build_client()

    analyze_messages = [
        {
            "role": "system",
            "content": "Summarize the request intent in English within three lines.",
        },
        {"role": "user", "content": REQUEST},
    ]
    analysis = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(analyze_messages), temperature=0.1
        )
        .choices[0]
        .message
    )

    draft_messages = [
        {
            "role": "system",
            "content": "Write a short English proposal email from the provided analysis.",
        },
        {"role": "user", "content": f"Request: {REQUEST}\n\nAnalysis: {analysis}"},
    ]
    draft = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(draft_messages), temperature=0.3
        )
        .choices[0]
        .message
    )

    print_section("Intent analysis")
    print(analysis)
    print_section("Draft email")
    print(draft)


if __name__ == "__main__":
    run_sequential_chain()
