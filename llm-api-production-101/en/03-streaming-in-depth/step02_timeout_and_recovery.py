"""Llm Api Production 101 - Episode 2: Timeout and recovery."""

import os
import time

from groq import APIStatusError, Groq


def stream_with_timeout(client: Groq, prompt: str, timeout_sec: float = 10.0) -> str:
    """Stream with timeout."""
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    parts: list[str] = []
    deadline = time.monotonic() + timeout_sec

    try:
        for chunk in stream:
            if time.monotonic() > deadline:
                print("\n[timeout: returning the partial response collected so far]")
                break
            delta = chunk.choices[0].delta.content
            if delta:
                parts.append(delta)
                print(delta, end="", flush=True)
    except APIStatusError as exc:
        print(f"\n[APIStatusError {exc.status_code}] {exc.message}")

    return "".join(parts)


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    result = stream_with_timeout(
        client,
        "Explain the Python asyncio event loop.",
        timeout_sec=8.0,
    )
    print(f"\n\ncollected_chars: {len(result)}")


if __name__ == "__main__":
    main()
