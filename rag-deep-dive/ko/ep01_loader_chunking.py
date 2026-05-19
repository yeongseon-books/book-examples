"""Rag Deep Dive - Episode 1: Loader chunking."""

from __future__ import annotations

from common import load_markdown_fixtures, sentence_split


def fixed_size_chunks(text: str, size: int = 80, overlap: int = 20) -> list[str]:
    """Fixed size chunks."""
    if size <= overlap:
        raise ValueError("size must be greater than overlap")
    out: list[str] = []
    step = size - overlap
    for i in range(0, len(text), step):
        chunk = text[i : i + size]
        if chunk:
            out.append(chunk)
        if i + size >= len(text):
            break
    return out


def sentence_aware_chunks(text: str, max_chars: int = 120) -> list[str]:
    """Sentence aware chunks."""
    sentences = sentence_split(text)
    chunks: list[str] = []
    cur = ""
    for s in sentences:
        if len(cur) + len(s) + 1 <= max_chars:
            cur = (cur + " " + s).strip()
        else:
            if cur:
                chunks.append(cur)
            cur = s
    if cur:
        chunks.append(cur)
    return chunks


def run(fixtures_dir: str = "fixtures") -> dict[str, list[str]]:
    """Run."""
    docs = load_markdown_fixtures(fixtures_dir)
    return {name: sentence_aware_chunks(text) for name, text in docs.items()}


if __name__ == "__main__":
    print(run())
