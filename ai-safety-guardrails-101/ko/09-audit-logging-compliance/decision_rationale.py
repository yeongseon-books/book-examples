"""Generated from book-content article."""

def log_decision(request_id: str, query: str, chunks: list[dict], answer: str, params: dict):
    audit_db.insert({
        "request_id": request_id,
        "type": "rag_decision",
        "query_hash": sha256(query.encode()).hexdigest(),
        "chunk_ids": [c["id"] for c in chunks],
        "chunk_scores": [c["score"] for c in chunks],
        "model": params["model"],
        "temperature": params["temperature"],
        "seed": params.get("seed"),
        "answer_hash": sha256(answer.encode()).hexdigest(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })
