# rag/faithfulness.py
FAITHFULNESS_PROMPT = """Decompose the answer into atomic claims and check whether each is supported by the context.

Question: {question}
Context: {context}
Answer: {answer}

Output JSON:
{{
  "claims": [
    {{"claim": "...", "supported_by_context": true/false}},
    ...
  ]
}}
"""

def faithfulness(question: str, context: str, answer: str) -> float:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": FAITHFULNESS_PROMPT.format(
            question=question, context=context, answer=answer
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
