"""Generated from book-content article."""

from collections import Counter
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

def exact_match_normalized(pred: str, expected: str) -> int:
    normalize = lambda s: s.lower().strip().rstrip(".!?")
    return int(normalize(pred) == normalize(expected))

def token_f1(pred: str, expected: str) -> float:
    pred_tokens = Counter(pred.lower().split())
    exp_tokens = Counter(expected.lower().split())
    common = pred_tokens & exp_tokens
    overlap = sum(common.values())
    if overlap == 0:
        return 0.0
    precision = overlap / sum(pred_tokens.values())
    recall = overlap / sum(exp_tokens.values())
    return 2 * precision * recall / (precision + recall)

scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
smooth = SmoothingFunction().method1

cases = [
    ("Seoul", "Seoul"),
    ("The capital of Korea is Seoul.", "Seoul"),
    ("A cat is sitting on a mat", "The cat sat on the mat"),
]

for pred, expected in cases:
    bleu = sentence_bleu(
        [expected.lower().split()],
        pred.lower().split(),
        smoothing_function=smooth,
    )
    rouge = scorer.score(expected, pred)
    print(
        {
            "prediction": pred,
            "expected": expected,
            "exact_match": exact_match_normalized(pred, expected),
            "token_f1": round(token_f1(pred, expected), 3),
            "bleu": round(bleu, 3),
            "rouge1_f": round(rouge["rouge1"].fmeasure, 3),
            "rougeL_f": round(rouge["rougeL"].fmeasure, 3),
        }
    )
