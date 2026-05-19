"""Llm Api Production 101 - Episode 2: Schema validation."""

import json
import os

from groq import Groq

SCHEMA_INSTRUCTION = """
Respond with JSON matching this schema exactly:
{
  "category": "billing" | "technical" | "account",
  "priority": "low" | "medium" | "high",
  "summary": "<single-sentence summary>"
}
"""


def classify_ticket(client: Groq, ticket: str) -> dict:
    """Classify ticket."""
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SCHEMA_INSTRUCTION},
            {"role": "user", "content": ticket},
        ],
        response_format={"type": "json_object"},
        temperature=0.0,
    )
    return json.loads(completion.choices[0].message.content or "{}")


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    tickets = [
        "This month's bill is more than double last month.",
        "Clicking the CSV upload button returns a 500 error.",
        "I changed my password but I still cannot sign in.",
    ]

    for ticket in tickets:
        result = classify_ticket(client, ticket)
        print(f"ticket: {ticket}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print()

        assert result.get("category") in {"billing", "technical", "account"}
        assert result.get("priority") in {"low", "medium", "high"}
        assert isinstance(result.get("summary"), str)

    print("Schema validation passed.")


if __name__ == "__main__":
    main()
