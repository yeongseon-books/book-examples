from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np


def _seed_from_bytes(data: bytes, namespace: str) -> int:
    digest = hashlib.sha256(namespace.encode("utf-8") + data).digest()
    return int.from_bytes(digest[:8], "little", signed=False)


def _to_bytes(value: bytes | str | np.ndarray) -> bytes:
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return value.encode("utf-8")
    return value.tobytes()


def l2_normalize(vector: np.ndarray) -> np.ndarray:
    arr = np.asarray(vector, dtype=np.float32)
    norm = float(np.linalg.norm(arr))
    if norm == 0.0:
        return arr
    return arr / norm


def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(l2_normalize(a), l2_normalize(b)))


@dataclass
class VectorIndex:
    vectors: np.ndarray
    items: list[dict[str, str]]

    def search(self, query: np.ndarray, top_k: int = 1) -> list[dict[str, str]]:
        scores = self.vectors @ l2_normalize(query)
        indices = np.argsort(-scores)[:top_k]
        return [self.items[int(i)] for i in indices]


def vector_index(items: list[dict[str, str]], vectors: np.ndarray) -> VectorIndex:
    normalized = np.vstack([l2_normalize(v) for v in vectors]).astype(np.float32)
    return VectorIndex(vectors=normalized, items=items)


class MockImageEncoder:
    dim: int = 512

    def encode(self, image: bytes | str | np.ndarray) -> np.ndarray:
        seed = _seed_from_bytes(_to_bytes(image), "image")
        rng = np.random.default_rng(seed)
        vec = rng.standard_normal(self.dim, dtype=np.float32)
        return l2_normalize(vec)


class MockTextEncoder:
    dim: int = 512

    def encode(self, text: str) -> np.ndarray:
        seed = _seed_from_bytes(text.encode("utf-8"), "text")
        rng = np.random.default_rng(seed)
        vec = rng.standard_normal(self.dim, dtype=np.float32)
        return l2_normalize(vec)


class MockAudioEncoder:
    dim: int = 512

    def encode(self, audio: bytes | np.ndarray) -> np.ndarray:
        seed = _seed_from_bytes(_to_bytes(audio), "audio")
        rng = np.random.default_rng(seed)
        vec = rng.standard_normal(self.dim, dtype=np.float32)
        return l2_normalize(vec)


class MockVLM:
    def __init__(self) -> None:
        self.templates = {
            0: "a simple synthetic grid image",
            1: "a bright block pattern with contrast",
            2: "a low-resolution texture with repeated cells",
            3: "a tiny grayscale checkerboard",
        }

    def generate(self, image: bytes | str | np.ndarray, text_prompt: str) -> str:
        bucket = _seed_from_bytes(_to_bytes(image), "vlm") % 4
        base = self.templates[int(bucket)]
        return f"{base}; prompt={text_prompt.strip() or 'none'}"


class MockOCR:
    def __init__(self, mapping: dict[str, str] | None = None) -> None:
        self.mapping = mapping or {
            "receipt": "latte 4500\nbagel 3200\ntotal 7700",
            "invoice": "invoice id: inv-101\namount: 120000",
            "label": "fragile handle with care",
        }

    def extract(self, key: str, _: bytes | np.ndarray) -> str:
        return self.mapping.get(key, "")


class MockDiffusion:
    def generate(self, prompt: str, shape: tuple[int, int] = (8, 8)) -> np.ndarray:
        h, w = shape
        seed = _seed_from_bytes(prompt.encode("utf-8"), "diffusion")
        grid = np.fromfunction(
            lambda i, j: (i * 17 + j * 31 + seed % 251) % 255, (h, w), dtype=int
        )
        return grid.astype(np.uint8)


class MultimodalRAG:
    def __init__(self, corpus: list[dict[str, str]]) -> None:
        self.image_encoder = MockImageEncoder()
        self.text_encoder = MockTextEncoder()
        self.corpus = corpus
        vectors = [self._joint(item["image"], item["text"]) for item in corpus]
        self.index = vector_index(corpus, np.vstack(vectors))

    def _joint(self, image_key: str, text: str) -> np.ndarray:
        image_vec = self.image_encoder.encode(image_key)
        text_vec = self.text_encoder.encode(text)
        return l2_normalize((image_vec + text_vec) / 2.0)

    def retrieve(
        self, image_key: str, query_text: str, top_k: int = 1
    ) -> list[dict[str, str]]:
        query = self._joint(image_key, query_text)
        return self.index.search(query, top_k=top_k)


class VideoSummarizer:
    def pool(
        self, frame_embeddings: list[np.ndarray], mode: str = "mean"
    ) -> np.ndarray:
        arr = np.vstack(frame_embeddings)
        if mode == "max":
            return l2_normalize(arr.max(axis=0))
        return l2_normalize(arr.mean(axis=0))


class MultimodalApp:
    def __init__(self) -> None:
        self.image_encoder = MockImageEncoder()
        self.text_encoder = MockTextEncoder()
        self.audio_encoder = MockAudioEncoder()
        self.vlm = MockVLM()
        self.ocr = MockOCR()
        self.diffusion = MockDiffusion()
        self.rag = MultimodalRAG(
            corpus=[
                {"id": "doc-1", "image": "grid-a", "text": "receipt with totals"},
                {
                    "id": "doc-2",
                    "image": "grid-b",
                    "text": "diagram about multimodal fusion",
                },
                {"id": "doc-3", "image": "grid-c", "text": "audio transcription notes"},
            ]
        )

    def query(
        self, image_key: str, question: str, audio: bytes | np.ndarray | None = None
    ) -> dict[str, object]:
        caption = self.vlm.generate(image_key, question)
        ocr_text = self.ocr.extract("receipt", b"dummy")
        hits = self.rag.retrieve(image_key, question, top_k=1)
        audio_vec = self.audio_encoder.encode(
            audio if audio is not None else b"silence"
        )
        return {
            "caption": caption,
            "ocr": ocr_text,
            "top_hit": hits[0]["id"],
            "audio_norm": float(np.linalg.norm(audio_vec)),
        }


def synthetic_image(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 255, size=(8, 8), dtype=np.uint8)


def synthetic_audio(
    freq: float = 220.0, length: int = 1600, sample_rate: int = 16000
) -> np.ndarray:
    t = np.arange(length, dtype=np.float32) / float(sample_rate)
    return np.sin(2.0 * np.pi * freq * t).astype(np.float32)
