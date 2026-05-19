"""
Step 01 — Basic stream=True pattern
======================================================
Run:
    python step01_basic_stream.py

Add stream=True and iterate over the stream
to inspect each chunk object directly.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a concise Python tutor."},
            {
                "role": "user",
                "content": "Explain Python generators in no more than five sentences.",
            },
        ],
        temperature=0.3,
        stream=True,
    )

    for chunk in stream:
        print(chunk)


if __name__ == "__main__":
    main()
