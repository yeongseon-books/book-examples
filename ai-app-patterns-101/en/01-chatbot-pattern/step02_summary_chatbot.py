from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

SYSTEM_PROMPT = "You are an AI coach. Use the running summary to keep answers consistent across turns."


def summarize_history(client, history: list[dict[str, str]]) -> str:
    summary_messages = [
        {
            "role": "system",
            "content": "Compress the conversation into an English summary with at most five sentences.",
        },
        {"role": "user", "content": str(history)},
    ]
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=as_messages(summary_messages),
        temperature=0.1,
    )
    return response_text(response.choices[0].message)


def run_summary_chatbot() -> None:
    client = build_client()
    history: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]
    rolling_summary = "No summary yet"

    user_turns = [
        "Explain the difference between RAG and plain search.",
        "What should I watch from a cost perspective?",
        "Continue from that and recommend a strategy for a small team.",
    ]

    for idx, turn in enumerate(user_turns, start=1):
        if len(history) > 5:
            rolling_summary = summarize_history(client, history[1:])
            history = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "system",
                    "content": f"Conversation summary: {rolling_summary}",
                },
            ]

        history.append({"role": "user", "content": turn})
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(history),
            temperature=0.2,
        )
        answer = response_text(response.choices[0].message)
        history.append({"role": "assistant", "content": answer})

        print_section(f"Turn {idx}")
        print(f"Question: {turn}")
        print(f"Answer: {answer}")

    print_section("Final summary")
    print(rolling_summary)


if __name__ == "__main__":
    run_summary_chatbot()
