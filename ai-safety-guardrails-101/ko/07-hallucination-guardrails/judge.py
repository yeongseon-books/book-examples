"""Generated from book-content article."""

JUDGE_PROMPT = """Decide whether the CLAIM is supported by the EVIDENCE.
Reply with JSON: {"supported": true|false, "reason": "..."}.

CLAIM: {claim}

EVIDENCE:
\"\"\"{evidence}\"\"\"
"""

def judge_grounding(claim: str, evidence: str) -> dict:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": JUDGE_PROMPT.format(claim=claim, evidence=evidence)}],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return json.loads(resp.choices[0].message.content)
