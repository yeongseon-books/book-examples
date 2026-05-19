"""Ai Evaluation 101 - Episode 1: Deterministic metrics."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import bleu1_like, exact_match, rouge_l_like


def run() -> dict[str, float]:
    """Run."""
    reference = "rag combines retrieval and generation"
    pred_good = "rag combines retrieval and generation"
    pred_para = "retrieval and generation are combined by rag"
    return {
        "em_good": float(exact_match(pred_good, reference)),
        "em_para": float(exact_match(pred_para, reference)),
        "bleu_para": bleu1_like(pred_para, reference),
        "rouge_para": rouge_l_like(pred_para, reference),
    }


if __name__ == "__main__":
    print(run())
