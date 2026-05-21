"""Generated from book-content article."""

import json

CLAIM_PROMPT = """Decompose the answer below into atomic factual claims.
Each claim must be a single declarative sentence that can be verified independently.
Return JSON: {"claims": [{"id": 1, "text": "..."}, ...]}.

ANSWER:
\"\"\"{answer}\"\"\"
"""

def extract_claims(answer: str) -> list[dict]:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": CLAIM_PROMPT.format(answer=answer)}],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return json.loads(resp.choices[0].message.content)["claims"]
