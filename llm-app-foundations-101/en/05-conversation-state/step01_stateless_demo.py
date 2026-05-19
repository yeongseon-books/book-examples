"""
Step 01 — Show the stateless nature of API calls
======================================================
Run:
    python step01_stateless_demo.py

Tell the model a name in the first request,
then omit the history in the second request to show that it does not remember automatically.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    first = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "My name is Minjun. Please remember it."}
        ],
        temperature=0.0,
    )
    print("[turn 1 — provide the name]")
    print(first.choices[0].message.content)
    print()

    second = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "What was my name?"}],
        temperature=0.0,
    )
    print("[turn 2 — ask again without history]")
    print(second.choices[0].message.content)
    print()
    print(
        "The model does not remember previous requests unless you send the history again."
    )


if __name__ == "__main__":
    main()
