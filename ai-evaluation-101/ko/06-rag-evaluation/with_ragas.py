# rag/with_ragas.py
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    context_precision,
    context_recall,
    faithfulness,
)

dataset = Dataset.from_dict({
    "question":     ["What is RAG?", ...],
    "ground_truth": ["RAG combines retrieval with generation...", ...],
    "answer":       ["RAG is a retrieval-based generation technique...", ...],
    "contexts":     [["RAG is...", "Retrieval is..."], ...],
})

result = evaluate(
    dataset,
    metrics=[context_recall, context_precision, faithfulness, answer_relevancy],
)
print(result)
# {'context_recall': 0.85, 'context_precision': 0.72, 'faithfulness': 0.91, 'answer_relevancy': 0.88}
