"""Ai Data Preparation 101 - 5편: tokenization chunking 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import chunk_tokens, tokenize


def run() -> dict[str, int]:
    """Run."""
    text = "Tokenization and chunking are core for RAG quality and context efficiency."
    tokens = tokenize(text)
    chunks = chunk_tokens(tokens, chunk_size=5, overlap=2)
    return {
        "tokens": len(tokens),
        "chunks": len(chunks),
        "first_chunk_size": len(chunks[0]),
    }


if __name__ == "__main__":
    print(run())
