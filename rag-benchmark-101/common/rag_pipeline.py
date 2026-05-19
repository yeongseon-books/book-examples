from __future__ import annotations

import json
import os
import time

from groq import Groq

from common.embeddings import build_embeddings, cosine_ranking
from common.judge import evaluate_generation
from common.models import BenchmarkConfig, FullBenchmarkResult, PipelineCase
from common.retrieval import compute_retrieval_metrics


def answer_with_groq(
    question: str,
    context: str,
    prompt_template: str,
    model: str = "llama-3.1-8b-instant",
) -> str:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model=model,
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": "Answer only from the provided context. If the answer is missing, say so clearly.",
            },
            {
                "role": "user",
                "content": prompt_template.format(question=question, context=context),
            },
        ],
    )
    return response.choices[0].message.content or ""


def run_pipeline_benchmark(
    language: str,
    corpus: list[dict[str, str]],
    test_cases: list[PipelineCase],
    config: BenchmarkConfig,
) -> FullBenchmarkResult:
    doc_ids = [doc["id"] for doc in corpus]
    doc_texts = [doc["text"] for doc in corpus]
    doc_vectors = build_embeddings(doc_texts, config.embedding_model)

    precisions: list[float] = []
    recalls: list[float] = []
    mrrs: list[float] = []
    faiths: list[float] = []
    relevances: list[float] = []
    latencies: list[float] = []

    for case in test_cases:
        started = time.perf_counter()
        query_vector = build_embeddings([case.question], config.embedding_model)[0]
        ranked_ids = cosine_ranking(query_vector, doc_vectors, doc_ids, config.top_k)
        retrieved_docs = [
            next(doc for doc in corpus if doc["id"] == doc_id) for doc_id in ranked_ids
        ]
        context = "\n\n".join(doc["text"] for doc in retrieved_docs)
        answer = answer_with_groq(case.question, context, config.answer_prompt)
        latencies.append((time.perf_counter() - started) * 1000)

        retrieval = compute_retrieval_metrics(
            ranked_ids, case.relevant_ids, config.top_k
        )
        judge = evaluate_generation(case.question, context, answer, language)
        precisions.append(retrieval.precision_at_k)
        recalls.append(retrieval.recall_at_k)
        mrrs.append(retrieval.mrr)
        faiths.append(judge["faithfulness"].score)
        relevances.append(judge["answer_relevance"].score)

    def average(values: list[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    return FullBenchmarkResult(
        config_name=config.name,
        precision_at_k=average(precisions),
        recall_at_k=average(recalls),
        mrr=average(mrrs),
        faithfulness=average(faiths),
        answer_relevance=average(relevances),
        average_latency_ms=average(latencies),
        total_queries=len(test_cases),
    )


def result_to_json(result: FullBenchmarkResult) -> str:
    return json.dumps(result.summary(), indent=2, ensure_ascii=False)
