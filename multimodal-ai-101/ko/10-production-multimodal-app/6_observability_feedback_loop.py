"""Generated from book-content article."""

from prometheus_client import Histogram, Counter

inference_latency = Histogram(
    "multimodal_inference_seconds", "End-to-end inference time",
    ["model", "modality"], buckets=[0.1, 0.5, 1, 2, 5, 10, 30],
)
cache_hit = Counter("multimodal_cache_hit_total", "Cache hits", ["tier"])
hallucination_flag = Counter("multimodal_hallucination_total", "Detected hallucinations")
