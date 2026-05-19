"""
Step 01 — Read the usage fields
======================================================
Run:
    python step01_read_usage.py

After an API call, print usage.prompt_tokens,
completion_tokens, total_tokens, and finish_reason.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Explain Python decorators in no more than two paragraphs.",
            }
        ],
    )

    usage = completion.usage
    if usage is None:
        raise RuntimeError("Did not receive usage metadata.")

    print(completion.choices[0].message.content)
    print()
    print(f"finish_reason={completion.choices[0].finish_reason}")
    print(f"prompt_tokens={usage.prompt_tokens}")
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"total_tokens={usage.total_tokens}")


if __name__ == "__main__":
    main()


# Expected output:
# Prompt tokens: 24
# Completion tokens: 156
# Total tokens: 180
# Estimated cost: $0.000036
