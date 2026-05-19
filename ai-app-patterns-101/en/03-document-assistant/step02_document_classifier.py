"""Ai App Patterns 101 - Episode 2: Document classifier."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

DOCUMENTS = [
    "A customer sent the payment failure screen and error timestamp. The team needs to inspect gateway logs.",
    "This is a draft proposal for next quarter's recommendation experiment budget and expected metrics.",
    "Please add local run instructions and an FAQ to the new engineer onboarding guide.",
]


def classify_documents() -> None:
    """Classify documents."""
    client = build_client()
    system_prompt = "Classify the document as 'operational issue', 'planning document', or 'internal guide', then explain why in one line."

    for idx, document in enumerate(DOCUMENTS, start=1):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": document},
        ]
        response = client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.1
        )
        print_section(f"Document {idx}")
        print(document)
        print(response_text(response.choices[0].message))


if __name__ == "__main__":
    classify_documents()
