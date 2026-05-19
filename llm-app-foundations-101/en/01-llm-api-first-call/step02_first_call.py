"""
Step 02 — First API call
======================================================
Run:
    python step02_first_call.py

Create a Groq client, send a message to llama-3.1-8b-instant,
and print the response text.
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
                "content": "Explain Python list comprehensions in one paragraph.",
            }
        ],
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
