"""
Step 04 — Long prompt guard and finish_reason
======================================================
Run:
    python step04_long_prompt_guard.py

Estimate a long prompt first, call the API,
then compare usage and inspect finish_reason.
"""

import os

import tiktoken
from groq import Groq


def estimate_tokens(text: str) -> int:
    """Estimate tokens."""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    long_text = " ".join(
        [
            "Explain why a Python web application should keep both request logs and exception logs."
        ]
        * 200
    )
    instruction = (
        "Read the text below and summarize only the key points in ten bullet points."
    )
    user_content = instruction + "\n\n" + long_text

    estimated = estimate_tokens(user_content)
    print(f"estimated_prompt_tokens={estimated}")

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_content}],
        max_tokens=60,
    )

    choice = completion.choices[0]
    usage = completion.usage
    if usage is None:
        raise RuntimeError("Did not receive usage metadata.")

    print(choice.message.content)
    print()
    print(f"prompt_tokens={usage.prompt_tokens}")
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"total_tokens={usage.total_tokens}")
    print(f"finish_reason={choice.finish_reason}")

    if choice.finish_reason == "length":
        print("Warning: the output hit the length limit and stopped early.")


if __name__ == "__main__":
    main()


# Expected output:
# Input tokens: 3847
# Max allowed: 4096
# ⚠ Trimming prompt to fit within budget...
# Trimmed tokens: 3900 → 2048
# Response generated successfully.
