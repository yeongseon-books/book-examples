"""
Step 05 — Detect token budget overflow
======================================================
Run:
    python step05_token_budget_guard.py

Use a rough character-based estimate to check whether a message list
exceeds the token budget, then trim history if needed.
"""


def rough_token_count(messages: list[dict[str, str]]) -> int:
    total_chars = sum(len(message["content"]) for message in messages)
    overhead = len(messages) * 12
    return (total_chars // 4) + overhead


def enforce_budget(
    messages: list[dict[str, str]],
    max_input_tokens: int = 6000,
) -> list[dict[str, str]]:
    if rough_token_count(messages) <= max_input_tokens:
        return messages

    trimmed = messages[:1] + messages[-8:]
    if rough_token_count(trimmed) <= max_input_tokens:
        print(f"Trimmed {len(messages) - len(trimmed)} messages from the history.")
        return trimmed

    raise ValueError(
        "The conversation history is too long. You need a more aggressive summary."
    )


def main() -> None:
    system = {"role": "system", "content": "You are a helpful assistant."}
    short_history = [system] + [
        {
            "role": "user" if index % 2 == 0 else "assistant",
            "content": f"Message {index}",
        }
        for index in range(10)
    ]
    long_history = [system] + [
        {"role": "user" if index % 2 == 0 else "assistant", "content": "x" * 200}
        for index in range(200)
    ]

    print(f"short_history rough tokens: {rough_token_count(short_history)}")
    result = enforce_budget(short_history)
    print(f"after enforce: {len(result)} messages\n")

    print(f"long_history rough tokens: {rough_token_count(long_history)}")
    try:
        result = enforce_budget(long_history, max_input_tokens=3000)
        print(f"after enforce: {len(result)} messages")
    except ValueError as exc:
        print(f"Exception: {exc}")


if __name__ == "__main__":
    main()
