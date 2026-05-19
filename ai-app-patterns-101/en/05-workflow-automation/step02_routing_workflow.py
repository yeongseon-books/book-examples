"""Ai App Patterns 101 - Episode 2: Routing workflow."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

REQUESTS = [
    "Write a short customer-facing notice for a payment outage.",
    "Suggest three experiment ideas for next quarter.",
]


def route_request(client, request: str) -> tuple[str, str]:
    """Route request."""
    classifier_messages = [
        {
            "role": "system",
            "content": "Classify the input as only 'incident' or 'planning'.",
        },
        {"role": "user", "content": request},
    ]
    route = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(classifier_messages),
            temperature=0,
        )
        .choices[0]
        .message
    ).lower()

    if "incident" in route:
        writer_prompt = "Write a customer outage notice in English. Prioritize current status and next update over speculation."
        label = "incident"
    else:
        writer_prompt = (
            "Write the response as English bullet points for an experiment proposal."
        )
        label = "planning"

    writer_messages = [
        {"role": "system", "content": writer_prompt},
        {"role": "user", "content": request},
    ]
    result = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(writer_messages), temperature=0.3
        )
        .choices[0]
        .message
    )
    return label, result


def run_routing_workflow() -> None:
    """Run routing workflow."""
    client = build_client()
    for request in REQUESTS:
        route, output = route_request(client, request)
        print_section(f"Route: {route}")
        print(request)
        print(output)


if __name__ == "__main__":
    run_routing_workflow()
