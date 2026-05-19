from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import faiss
import fitz  # pyright: ignore[reportMissingImports]
import numpy as np


@dataclass
class SearchHit:
    score: float
    metadata: dict[str, Any]


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def write_text(path: Path, content: str) -> Path:
    ensure_parent(path).write_text(content, encoding="utf-8")
    return path


def write_json(path: Path, payload: Any) -> Path:
    ensure_parent(path).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def write_csv(path: Path, rows: list[dict[str, Any]]) -> Path:
    ensure_parent(path)
    if not rows:
        raise ValueError("rows must not be empty")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def slugify(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    return text.strip("-") or "section"


def sentence_split(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?다])\s+", text.strip())
    return [part.strip() for part in parts if part.strip()]


def word_windows(words: list[str], size: int, overlap: int) -> list[str]:
    if size <= 0:
        raise ValueError("size must be positive")
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    step = size - overlap
    windows: list[str] = []
    for start in range(0, len(words), step):
        chunk_words = words[start : start + size]
        if not chunk_words:
            continue
        windows.append(" ".join(chunk_words))
        if start + size >= len(words):
            break
    return windows


def fixed_chunks(text: str, *, size: int, overlap: int) -> list[str]:
    return word_windows(text.split(), size=size, overlap=overlap)


def recursive_chunks(text: str, *, size: int, overlap: int) -> list[str]:
    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0
    for paragraph in paragraphs:
        paragraph_words = paragraph.split()
        if len(paragraph_words) > size:
            for sentence in sentence_split(paragraph):
                sentence_words = sentence.split()
                if current_words + len(sentence_words) <= size:
                    current.append(sentence)
                    current_words += len(sentence_words)
                    continue
                if current:
                    chunks.append(" ".join(current))
                current = sentence_words[-overlap:] if overlap > 0 else []
                current = [" ".join(current)] if current else []
                current_words = len(current[0].split()) if current else 0
                if len(sentence_words) >= size:
                    chunks.extend(
                        word_windows(sentence_words, size=size, overlap=overlap)
                    )
                    current = []
                    current_words = 0
                else:
                    current.append(sentence)
                    current_words += len(sentence_words)
            continue
        if current_words + len(paragraph_words) <= size:
            current.append(paragraph)
            current_words += len(paragraph_words)
            continue
        if current:
            chunks.append("\n\n".join(current))
        carry_words = " ".join(current).split()
        carry = carry_words[-overlap:] if overlap > 0 else []
        current = [" ".join(carry), paragraph] if carry else [paragraph]
        current = [part for part in current if part]
        current_words = len(" ".join(current).split())
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def heading_chunks(markdown_text: str) -> list[dict[str, str]]:
    chunks: list[dict[str, str]] = []
    current_heading = "document"
    buffer: list[str] = []
    for line in markdown_text.splitlines():
        if line.startswith("#"):
            if buffer:
                chunks.append(
                    {
                        "heading": current_heading,
                        "slug": slugify(current_heading),
                        "text": "\n".join(buffer).strip(),
                    }
                )
                buffer = []
            current_heading = line.lstrip("# ").strip()
            continue
        buffer.append(line)
    if buffer:
        chunks.append(
            {
                "heading": current_heading,
                "slug": slugify(current_heading),
                "text": "\n".join(buffer).strip(),
            }
        )
    return [chunk for chunk in chunks if chunk["text"]]


def make_demo_pdf(
    path: Path,
    *,
    title: str,
    author: str,
    subject: str,
    pages: list[str],
    language: str,
) -> Path:
    ensure_parent(path)
    document = fitz.open()
    for page_number, text in enumerate(pages, start=1):
        page = document.new_page()
        page.insert_text((72, 72), f"{title} - {page_number}", fontsize=18)
        page.insert_textbox(
            fitz.Rect(72, 110, 540, 760),
            text,
            fontsize=11,
            lineheight=1.4,
        )
    document.set_metadata(
        {
            "title": title,
            "author": author,
            "subject": subject,
            "keywords": f"document-ingestion,{language}",
            "creator": "document-ingestion-101 examples",
        }
    )
    document.save(path)
    document.close()
    return path


def extract_pdf_pages(path: Path) -> tuple[dict[str, str], list[dict[str, Any]]]:
    document = fitz.open(path)
    raw_metadata = document.metadata or {}
    metadata = {
        "title": str(raw_metadata.get("title") or ""),
        "author": str(raw_metadata.get("author") or ""),
        "subject": str(raw_metadata.get("subject") or ""),
    }
    pages: list[dict[str, Any]] = []
    for page_index in range(document.page_count):
        index = page_index + 1
        page = document.load_page(page_index)
        text = str(page.get_text("text")).strip()
        pages.append(
            {
                "page": index,
                "text": text,
                "metadata": {
                    "source": str(path),
                    "page": index,
                    "total_pages": document.page_count,
                    "title": metadata["title"],
                    "author": metadata["author"],
                    "subject": metadata["subject"],
                },
            }
        )
    document.close()
    return metadata, pages


def hash_text(text: str, *, dim: int = 64) -> list[float]:
    vector = [0.0] * dim
    tokens = re.findall(r"[\w가-힣]+", text.lower())
    if not tokens:
        tokens = ["empty"]
    for token in tokens:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        bucket = digest[0] % dim
        sign = 1.0 if digest[1] % 2 == 0 else -1.0
        weight = 1.0 + digest[2] / 255.0
        vector[bucket] += sign * weight
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def build_faiss_index(
    items: list[dict[str, Any]], *, text_key: str = "text"
) -> tuple[faiss.IndexFlatIP, list[dict[str, Any]]]:
    if not items:
        raise ValueError("items must not be empty")
    vectors = [hash_text(str(item[text_key])) for item in items]
    dim = len(vectors[0])
    index = faiss.IndexFlatIP(dim)
    index.add(np.array(vectors, dtype="float32"))  # pyright: ignore[reportCallIssue]
    return index, items


def search_faiss(
    index: faiss.IndexFlatIP,
    items: list[dict[str, Any]],
    query: str,
    *,
    top_k: int,
    filters: dict[str, Any] | None = None,
) -> list[SearchHit]:
    query_vector = np.array([hash_text(query)], dtype="float32")
    scores, positions = index.search(query_vector, min(top_k * 3, len(items)))  # pyright: ignore[reportCallIssue]
    hits: list[SearchHit] = []
    for score, position in zip(scores[0], positions[0], strict=True):
        if position < 0:
            continue
        item = items[int(position)]
        metadata = item.get("metadata", {})
        if filters and any(
            metadata.get(key) != value for key, value in filters.items()
        ):
            continue
        hits.append(SearchHit(score=float(score), metadata=item))
        if len(hits) == top_k:
            break
    return hits


def fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class JsonStateStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> dict[str, dict[str, Any]]:
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, payload: dict[str, dict[str, Any]]) -> None:
        ensure_parent(self.path).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def upsert(self, source_path: Path, metadata: dict[str, Any]) -> None:
        current = self.load()
        current[str(source_path)] = metadata
        self.save(current)


def detect_change(current_hash: str, previous_hash: str | None) -> str:
    if previous_hash is None:
        return "new"
    if current_hash != previous_hash:
        return "updated"
    return "unchanged"


def load_text_document(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    return [
        {
            "text": text,
            "metadata": {"source": str(path), "format": path.suffix.lstrip(".")},
        }
    ]


def load_markdown_document(path: Path) -> list[dict[str, Any]]:
    chunks = heading_chunks(path.read_text(encoding="utf-8"))
    return [
        {
            "text": chunk["text"],
            "metadata": {
                "source": str(path),
                "format": "md",
                "heading": chunk["heading"],
                "section_slug": chunk["slug"],
            },
        }
        for chunk in chunks
    ]


def load_json_document(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        records = payload
    else:
        records = [payload]
    documents: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        documents.append(
            {
                "text": json.dumps(record, ensure_ascii=False),
                "metadata": {"source": str(path), "format": "json", "row": index},
            }
        )
    return documents


def load_csv_document(path: Path) -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader, start=1):
            documents.append(
                {
                    "text": ", ".join(f"{key}: {value}" for key, value in row.items()),
                    "metadata": {"source": str(path), "format": "csv", "row": index},
                }
            )
    return documents


def load_pdf_document(path: Path) -> list[dict[str, Any]]:
    _, pages = extract_pdf_pages(path)
    return [
        {"text": page["text"], "metadata": page["metadata"] | {"format": "pdf"}}
        for page in pages
    ]


def route_document(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    loaders = {
        ".txt": load_text_document,
        ".md": load_markdown_document,
        ".json": load_json_document,
        ".csv": load_csv_document,
        ".pdf": load_pdf_document,
    }
    loader = loaders.get(suffix)
    if loader is None:
        raise ValueError(f"unsupported format: {suffix}")
    return loader(path)


def incremental_scan(
    paths: Iterable[Path], store: JsonStateStore
) -> list[dict[str, Any]]:
    previous = store.load()
    changes: list[dict[str, Any]] = []
    for path in paths:
        current_hash = fingerprint(path)
        old = previous.get(str(path))
        status = detect_change(current_hash, old["fingerprint"] if old else None)
        if status == "unchanged":
            continue
        changes.append({"path": path, "status": status, "fingerprint": current_hash})
        store.upsert(
            path,
            {
                "fingerprint": current_hash,
                "size": path.stat().st_size,
            },
        )
    return changes
