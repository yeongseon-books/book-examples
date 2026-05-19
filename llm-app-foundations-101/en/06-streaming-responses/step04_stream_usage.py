"""
Step 04 — Read usage from the last chunk
======================================================
Run:
    python step04_stream_usage.py

Track the final chunk and read token usage
from x_groq.usage when it is available.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Explain Python decorators."}],
        stream=True,
    )

    parts: list[str] = []
    last_chunk = None

    for chunk in stream:
        last_chunk = chunk
        delta = chunk.choices[0].delta.content
        if delta:
            parts.append(delta)
            print(delta, end="", flush=True)

    print("\n---")
    print("".join(parts))

    usage = None
    if last_chunk is not None:
        groq_meta = getattr(last_chunk, "x_groq", None)
        if groq_meta is not None:
            usage = getattr(groq_meta, "usage", None)

    if usage is not None:
        print(f"prompt_tokens: {usage.prompt_tokens}")
        print(f"completion_tokens: {usage.completion_tokens}")
        print(f"total_tokens: {usage.total_tokens}")
    else:
        print("Usage metadata was not present in the final chunk.")


if __name__ == "__main__":
    main()
