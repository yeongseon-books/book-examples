# LLM Fine-tuning 101 (5/6): 모델 평가

Llm Finetuning 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 파인튜닝 직후 가장 먼저 봐야 할 정량 신호인 perplexity는 어떻게 계산할까요?
- 학습 전후 perplexity 비교만으로는 왜 평가가 충분하지 않을까요?
- 작은 데모 모델에서도 왜 별도의 평가 루프를 유지해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_groq_quality_comparison.py` | 예제 코드 |
| `step02_bleu_rouge_from_scratch.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-evaluation/step01_groq_quality_comparison.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/05-evaluation.md)
