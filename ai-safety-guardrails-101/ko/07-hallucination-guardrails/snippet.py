"""Generated from book-content article."""

def verify_grounding(answer: str, chunks: list[dict]) -> dict:
    chunk_texts = [c["text"] for c in chunks]
    chunk_ids = {c["id"] for c in chunks}

    cite = citation_check(answer, chunk_ids)
    if cite["missing_chunks"] or cite["uncited_sentences"]:
        return {"ok": False, "stage": "citation", "detail": cite}

    claims = extract_claims(answer)
    nli_result = grounded(claims, chunk_texts)
    if not nli_result["ok"]:
        rechecked = []
        for f in nli_result["failures"]:
            best_chunk = max(chunk_texts, key=lambda ch: entails(ch, f["claim"]))
            verdict = judge_grounding(f["claim"], best_chunk)
            if not verdict["supported"]:
                rechecked.append(f["claim"])
        if rechecked:
            return {"ok": False, "stage": "semantic", "claims": rechecked}

    return {"ok": True}
