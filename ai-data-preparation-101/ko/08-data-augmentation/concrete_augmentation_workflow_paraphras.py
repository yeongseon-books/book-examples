"""Generated from book-content article."""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
paraphraser = pipeline(
    "text2text-generation",
    model="humarin/chatgpt_paraphraser_on_T5_base",
)

BANNED_SUBSTRINGS = ["환불 불가", "법적 조치", "계정 정지"]

def paraphrase_ko(text: str, n: int = 3) -> list[str]:
    outputs = paraphraser(
        text,
        num_return_sequences=n,
        num_beams=n + 2,
        do_sample=True,
        temperature=0.8,
        max_length=96,
    )
    return [o["generated_text"].strip() for o in outputs]

def semantic_similarity(a: str, b: str) -> float:
    va = embedder.encode([a])
    vb = embedder.encode([b])
    return float(cosine_similarity(va, vb)[0][0])

def build_augmented_rows(rows: list[dict]) -> list[dict]:
    augmented = []
    for row in rows:
        if row["label"] != "refund_delay":
            continue

        for candidate in paraphrase_ko(row["text"]):
            if any(bad in candidate for bad in BANNED_SUBSTRINGS):
                continue
            sim = semantic_similarity(row["text"], candidate)
            if sim < 0.78 or sim > 0.97:
                continue
            augmented.append({
                "text": candidate,
                "label": row["label"],
                "source_id": row["id"],
                "aug_method": "paraphrase",
                "similarity": round(sim, 4),
            })
    return augmented
