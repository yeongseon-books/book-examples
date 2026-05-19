"""
Step 04 — Split instruction, context, and output format
======================================================
Run:
    python step04_structured_prompt.py

Structure the user message into instruction, context,
and output format blocks for more repeatable prompting.
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
                "role": "system",
                "content": (
                    "You are a Python tutor for backend beginners. "
                    "Answer in English and do not guess."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Instruction: explain what a dataclass is.\n"
                    "Context: the reader knows Python syntax but is new to dataclasses.\n"
                    "Output format: 1) two-sentence explanation 2) code example in at most six lines 3) one line on when to use it"
                ),
            },
        ],
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()


# Expected output:
# {"name": "Python", "paradigm": "multi-paradigm", "typing": "dynamic",
#  "year": 1991, "creator": "Guido van Rossum"}
