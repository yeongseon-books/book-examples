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


# Expected output:
# A list comprehension in Python is a concise way to create lists by
# applying an expression to each item in an iterable, optionally filtering
# items with a condition. The syntax is [expression for item in iterable
# if condition]. For example, [x**2 for x in range(10) if x % 2 == 0]
# produces [0, 4, 16, 36, 64].
