# rag/answer_relevance.py
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

REVERSE_PROMPT = """Guess three questions that this answer would be a response to. One per line.

Answer: {answer}
"""

def answer_relevance(question: str, answer: str) -> float:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": REVERSE_PROMPT.format(answer=answer)}],
        temperature=0,
    )
    generated_qs = response.choices[0].message.content.strip().split("\n")[:3]

    emb_orig = model.encode([question])[0]
    embs_gen = model.encode(generated_qs)
    sims = [np.dot(emb_orig, eg) / (np.linalg.norm(emb_orig) * np.linalg.norm(eg))
            for eg in embs_gen]
    return float(np.mean(sims))
