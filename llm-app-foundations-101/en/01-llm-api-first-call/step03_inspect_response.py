"""
Step 03 — Inspect the response structure
======================================================
Run:
    python step03_inspect_response.py

Print the full response as JSON,
then read content, usage, model, and finish_reason.
"""

import json
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
                "content": "Explain the difference between an HTTP API and an SDK in three sentences.",
            }
        ],
    )

    print("=== raw response ===")
    print(json.dumps(completion.to_dict(), indent=2, ensure_ascii=False))

    print("\n=== key fields ===")
    text = completion.choices[0].message.content
    usage = completion.usage
    if usage is None:
        raise RuntimeError("Did not receive usage metadata.")

    print(f"content: {text}")
    print(f"model: {completion.model}")
    print(f"finish_reason: {completion.choices[0].finish_reason}")
    print(f"prompt_tokens: {usage.prompt_tokens}")
    print(f"completion_tokens: {usage.completion_tokens}")
    print(f"total_tokens: {usage.total_tokens}")
    print(f"request_id: {completion.id}")


if __name__ == "__main__":
    main()
