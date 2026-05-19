"""
Step 03 — Compare temperature values
======================================================
Run:
    python step03_temperature.py

Call the same prompt with temperature=0.0 and 0.9
to compare consistency and variety.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    prompt = "Introduce FastAPI to a developer who is learning it for the first time in three sentences."

    for temperature in (0.0, 0.9):
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an English technical blog editor. Answer concisely.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )
        print(f"[temperature={temperature}]")
        print(completion.choices[0].message.content)
        print()


if __name__ == "__main__":
    main()
