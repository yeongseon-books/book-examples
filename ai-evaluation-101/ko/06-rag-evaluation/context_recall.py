# rag/context_recall.py
from openai import OpenAI
import json

client = OpenAI()

RECALL_PROMPT = """Check whether every fact (claim) needed to produce the reference is present in the retrieved context.

Question: {question}
Reference answer: {reference}
Retrieved context:
{context}

First, decompose the reference into atomic claims. Then mark each claim as supported by the context (yes/no).

Output JSON:
{{
  "claims": [
    {{"claim": "...", "supported_by_context": true}},
    ...
  ]
}}
"""

def context_recall(question: str, reference: str, context: str) -> float:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": RECALL_PROMPT.format(
            question=question, reference=reference, context=context
        )}],
        temperature=0,
        response_format={"type": "json_object"},
    )
    data = json.loads(response.choices[0].message.content)
    claims = data["claims"]
    if not claims:
        return 0.0
    supported = sum(1 for c in claims if c["supported_by_context"])
    return supported / len(claims)
