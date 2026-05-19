"""BLEU/ROUGE 점수 계산기"""

from __future__ import annotations

import math

REFERENCES = [
    "the audit log is stored for ninety days on the pro plan",
    "password reset requires email verification",
]
HYPOTHESES = [
    "the audit log remains available for ninety days on pro",
    "reset the password with an email verification step",
]


def ngrams(tokens, n):
    return [tuple(tokens[index : index + n]) for index in range(len(tokens) - n + 1)]


def bleu_score(reference: str, hypothesis: str, max_n: int = 2) -> float:
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()
    precisions = []
    for n in range(1, max_n + 1):
        ref_counts = {
            gram: ngrams(ref_tokens, n).count(gram)
            for gram in set(ngrams(ref_tokens, n))
        }
        hyp_list = ngrams(hyp_tokens, n)
        hyp_counts = {gram: hyp_list.count(gram) for gram in set(hyp_list)}
        overlap = 0
        total = max(len(hyp_list), 1)
        for gram, count in hyp_counts.items():
            overlap += min(count, ref_counts.get(gram, 0))
        precisions.append(max(overlap / total, 1e-9))
    brevity_penalty = (
        1.0
        if len(hyp_tokens) > len(ref_tokens)
        else math.exp(1 - len(ref_tokens) / max(len(hyp_tokens), 1))
    )
    return brevity_penalty * math.exp(sum(math.log(p) for p in precisions) / max_n)


def rouge_l(reference: str, hypothesis: str) -> float:
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()
    dp = [[0] * (len(hyp_tokens) + 1) for _ in range(len(ref_tokens) + 1)]
    for i, ref_token in enumerate(ref_tokens, start=1):
        for j, hyp_token in enumerate(hyp_tokens, start=1):
            if ref_token == hyp_token:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[-1][-1]
    recall = lcs / max(len(ref_tokens), 1)
    precision = lcs / max(len(hyp_tokens), 1)
    if recall + precision == 0:
        return 0.0
    return 2 * recall * precision / (recall + precision)


def main() -> None:
    for index, (reference, hypothesis) in enumerate(
        zip(REFERENCES, HYPOTHESES, strict=False), start=1
    ):
        bleu = bleu_score(reference, hypothesis)
        rouge = rouge_l(reference, hypothesis)
        print(f"sample={index} bleu={bleu:.4f} rouge_l={rouge:.4f}")
    print(
        "BLEU는 n-gram 정밀도를, ROUGE-L은 가장 긴 공통 부분 수열 기반 재현율/정밀도 균형을 봅니다."
    )


if __name__ == "__main__":
    main()
