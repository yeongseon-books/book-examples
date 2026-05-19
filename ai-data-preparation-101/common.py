from __future__ import annotations

import hashlib
import random
import re
from dataclasses import dataclass
from datetime import datetime, timezone


Record = dict[str, str]


def mock_documents() -> list[Record]:
    return [
        {
            "id": "d1",
            "source": "blog",
            "text": "Data quality matters for reliable AI outputs.",
            "label": "good",
        },
        {
            "id": "d2",
            "source": "forum",
            "text": "Data quality matters for reliable AI outputs!",
            "label": "good",
        },
        {
            "id": "d3",
            "source": "log",
            "text": "BUY NOW!!! 999999 CLICK CLICK CLICK",
            "label": "bad",
        },
        {
            "id": "d4",
            "source": "ticket",
            "text": "Contact me at alice@example.com or 010-1234-5678.",
            "label": "bad",
        },
        {
            "id": "d5",
            "source": "wiki",
            "text": "Train and test sets should not overlap in identity.",
            "label": "good",
        },
    ]


def normalize_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text.strip())
    return text


def exact_dedup(texts: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for text in texts:
        key = hashlib.sha256(normalize_text(text).lower().encode("utf-8")).hexdigest()
        if key not in seen:
            seen.add(key)
            out.append(text)
    return out


def jaccard_similarity(a: str, b: str) -> float:
    ta = set(normalize_text(a).lower().split())
    tb = set(normalize_text(b).lower().split())
    if not ta and not tb:
        return 1.0
    return len(ta & tb) / max(len(ta | tb), 1)


def tokenize(text: str) -> list[str]:
    return [tok for tok in re.split(r"\W+", text.lower()) if tok]


def chunk_tokens(tokens: list[str], chunk_size: int, overlap: int) -> list[list[str]]:
    chunks: list[list[str]] = []
    step = max(chunk_size - overlap, 1)
    for i in range(0, len(tokens), step):
        chunk = tokens[i : i + chunk_size]
        if chunk:
            chunks.append(chunk)
        if i + chunk_size >= len(tokens):
            break
    return chunks


PII_PATTERNS: dict[str, re.Pattern[str]] = {
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "phone_kr": re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b"),
}


def redact_pii(text: str) -> str:
    out = text
    for name, pattern in PII_PATTERNS.items():
        out = pattern.sub(f"[{name.upper()}]", out)
    return out


def quality_signals(text: str) -> dict[str, float]:
    n = max(len(text), 1)
    symbol_ratio = sum(1 for c in text if not c.isalnum() and not c.isspace()) / n
    digit_ratio = sum(1 for c in text if c.isdigit()) / n
    upper_ratio = sum(1 for c in text if c.isupper()) / n
    return {
        "n_words": float(len(text.split())),
        "symbol_ratio": symbol_ratio,
        "digit_ratio": digit_ratio,
        "upper_ratio": upper_ratio,
    }


def seeded_shuffle(items: list[str], seed: int = 42) -> list[str]:
    out = list(items)
    rng = random.Random(seed)
    rng.shuffle(out)
    return out


@dataclass
class SplitResult:
    train: list[dict[str, str]]
    val: list[dict[str, str]]
    test: list[dict[str, str]]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
