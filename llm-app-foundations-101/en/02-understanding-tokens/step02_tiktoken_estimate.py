"""
Step 02 — Estimate token counts with tiktoken
======================================================
Run:
    python step02_tiktoken_estimate.py

Estimate token counts for strings and message lists
with the cl100k_base encoding.
"""

import tiktoken


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """Count tokens."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def estimate_messages_tokens(messages: list[dict[str, str]]) -> int:
    """Estimate messages tokens."""
    encoding = tiktoken.get_encoding("cl100k_base")
    serialized = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    return len(encoding.encode(serialized))


def main() -> None:
    """Main."""
    samples = [
        "hello world",
        "unbelievable",
        'print(user_profile[0]["email"])',
        "Estimating token length early makes long prompts safer to handle.",
    ]

    print("=== single string token counts ===")
    for text in samples:
        tokens = count_tokens(text)
        print(f"{tokens:3d} tokens | {text!r}")

    messages = [
        {"role": "system", "content": "You are a concise Python tutor."},
        {
            "role": "user",
            "content": "Explain the difference between a list and a tuple.",
        },
        {
            "role": "assistant",
            "content": "A list is mutable, while a tuple is immutable.",
        },
        {"role": "user", "content": "Please add a short code example too."},
    ]

    estimated = estimate_messages_tokens(messages)
    print("\n=== message token estimate ===")
    print(f"estimated_prompt_tokens={estimated}")
    print("The exact Groq billing count may differ slightly.")


if __name__ == "__main__":
    main()
