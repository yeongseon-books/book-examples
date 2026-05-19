"""Llm Api Production 101 - Episode 1: Json mode."""

import json
import os

from groq import Groq


def call_json_mode(client: Groq, prompt: str) -> dict:
    """Call json mode."""
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a data extraction assistant. Always return valid JSON only.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.1,
    )
    raw = completion.choices[0].message.content or "{}"
    return json.loads(raw)


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    result = call_json_mode(
        client,
        "Extract product=laptop, price=1500000, in_stock=true as JSON.",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    assert isinstance(result, dict), "Response is not a dict."
    print("JSON mode parsing succeeded.")


if __name__ == "__main__":
    main()


# Expected output:
# {"name": "Python", "paradigm": "multi-paradigm", "typing": "dynamic",
#  "year": 1991, "creator": "Guido van Rossum"}
