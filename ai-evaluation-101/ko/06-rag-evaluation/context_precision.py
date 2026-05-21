# rag/context_precision.py
PRECISION_PROMPT = """Is the following retrieved chunk needed to answer the question?

Question: {question}
Chunk: {chunk}

Output JSON: {{"relevant": true/false}}
"""

def context_precision(question: str, chunks: list[str]) -> float:
    relevant_count = 0
    for chunk in chunks:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # cheap model is fine for binary judgment
            messages=[{"role": "user", "content": PRECISION_PROMPT.format(
                question=question, chunk=chunk
            )}],
            temperature=0,
            response_format={"type": "json_object"},
        )
        if json.loads(response.choices[0].message.content)["relevant"]:
            relevant_count += 1
    return relevant_count / len(chunks)
