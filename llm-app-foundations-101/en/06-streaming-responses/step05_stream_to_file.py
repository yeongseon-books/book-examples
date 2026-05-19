"""
Step 05 — Write the stream to a file
======================================================
Run:
    python step05_stream_to_file.py

Write generated tokens to a file immediately,
then forward sentence-sized chunks to a consumer.
"""

import os
from collections.abc import Generator
from pathlib import Path

from groq import Groq


def sentence_chunks(stream) -> Generator[str, None, None]:
    buffer = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if not delta:
            continue
        buffer += delta
        while ". " in buffer:
            sentence, buffer = buffer.split(". ", 1)
            yield sentence + "."
    if buffer.strip():
        yield buffer


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    output_path = Path(__file__).with_name("summary.txt")

    with output_path.open("w", encoding="utf-8") as file:
        for chunk in client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "Explain vector databases in simple terms.",
                }
            ],
            stream=True,
        ):
            delta = chunk.choices[0].delta.content
            if delta:
                file.write(delta)
                file.flush()
                print(delta, end="", flush=True)

    print(f"\n\nSaved file: {output_path}")

    print("\n=== sentence pipeline ===")
    pipe_stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Explain vector databases in simple terms."}
        ],
        stream=True,
    )
    for sentence in sentence_chunks(pipe_stream):
        print(f"[consumer] {sentence}")


if __name__ == "__main__":
    main()
