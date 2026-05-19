"""Llm Api Production 101 - Episode 1: Chunk loop."""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Explain the four TCP/IP layers in one line each.",
            }
        ],
        stream=True,
    )

    parts: list[str] = []
    empty_count = 0

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta is None:
            empty_count += 1
            continue
        parts.append(delta)
        print(delta, end="", flush=True)

    print(f"\n\ntotal_chars={len(''.join(parts))} empty_chunks={empty_count}")


if __name__ == "__main__":
    main()
