"""Rag Deep Dive - Episode 4: Prompt builder."""

from __future__ import annotations


def build_prompt(question: str, contexts: list[str], budget_chars: int = 500) -> str:
    """Build prompt."""
    used = 0
    kept: list[str] = []
    for idx, c in enumerate(contexts, start=1):
        tag = f"[C{idx}] "
        line = tag + c.strip()
        if used + len(line) + 1 > budget_chars:
            break
        kept.append(line)
        used += len(line) + 1

    context_block = "\n".join(kept)
    return (
        "You are a helpful RAG assistant.\n"
        "Use only the context below and cite tags like [C1].\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {question}\n"
        "Answer:"
    )
