"""
Step 02 — Read and collect delta.content
======================================================
Run:
    python step02_collect_stream.py

Print delta.content immediately,
then collect the parts into a final response string.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Explain the difference between FastAPI and Flask from a beginner's perspective.",
            }
        ],
        temperature=0.2,
        stream=True,
    )

    parts: list[str] = []

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            parts.append(delta)

    final_text = "".join(parts)
    print("\n---")
    print(f"total chars: {len(final_text)}")


if __name__ == "__main__":
    main()
