"""Rag Benchmark 101 - Models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QueryGroundTruth:
    """Query ground truth."""

    query: str
    relevant_ids: set[str]
    topic: str


@dataclass(frozen=True)
class GenerationCase:
    """Generation case."""

    question: str
    context: str
    answer: str


@dataclass(frozen=True)
class PipelineCase:
    """Pipeline case."""

    question: str
    relevant_ids: set[str]
    reference_answer: str


@dataclass(frozen=True)
class EmbeddingCandidate:
    """Embedding candidate."""

    label: str
    model_name: str


@dataclass(frozen=True)
class VectorIndexCandidate:
    """Vector index candidate."""

    name: str
    factory: str


@dataclass(frozen=True)
class BenchmarkConfig:
    """Benchmark config."""

    name: str
    embedding_model: str
    top_k: int = 3
    answer_prompt: str = ""


@dataclass
class RetrievalMetrics:
    """Retrieval metrics."""

    precision_at_k: float
    recall_at_k: float
    mrr: float
    k: int

    @property
    def f1_at_k(self) -> float:
        """F1 at k."""
        total = self.precision_at_k + self.recall_at_k
        return (2 * self.precision_at_k * self.recall_at_k / total) if total else 0.0

    def summary(self) -> dict[str, float]:
        """Summary."""
        return {
            f"precision@{self.k}": round(self.precision_at_k, 4),
            f"recall@{self.k}": round(self.recall_at_k, 4),
            f"f1@{self.k}": round(self.f1_at_k, 4),
            "mrr": round(self.mrr, 4),
        }


@dataclass
class JudgeScore:
    """Judge score."""

    score: float
    reason: str


@dataclass
class FullBenchmarkResult:
    """Full benchmark result."""

    config_name: str
    precision_at_k: float
    recall_at_k: float
    mrr: float
    faithfulness: float
    answer_relevance: float
    average_latency_ms: float
    total_queries: int

    @property
    def retrieval_score(self) -> float:
        """Retrieval score."""
        return (self.precision_at_k + self.recall_at_k + self.mrr) / 3

    @property
    def generation_score(self) -> float:
        """Generation score."""
        return (self.faithfulness + self.answer_relevance) / 2

    @property
    def overall_score(self) -> float:
        """Overall score."""
        return (self.retrieval_score + self.generation_score) / 2

    def summary(self) -> dict[str, float | int | str]:
        """Summary."""
        return {
            "config": self.config_name,
            "overall_score": round(self.overall_score, 4),
            "retrieval_score": round(self.retrieval_score, 4),
            "generation_score": round(self.generation_score, 4),
            "precision@k": round(self.precision_at_k, 4),
            "recall@k": round(self.recall_at_k, 4),
            "mrr": round(self.mrr, 4),
            "faithfulness": round(self.faithfulness, 4),
            "answer_relevance": round(self.answer_relevance, 4),
            "average_latency_ms": round(self.average_latency_ms, 2),
            "total_queries": self.total_queries,
        }
