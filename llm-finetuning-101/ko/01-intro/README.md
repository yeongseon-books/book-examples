# LLM Fine-tuning 101 (1/6): LLM 파인튜닝 입문

Llm Finetuning 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- LoRA가 풀 파인튜닝보다 훨씬 가벼운 이유를 어떻게 계산할 수 있을까요?
- 프롬프트로 해결할 수 있는 문제와 파인튜닝이 필요한 문제를 어떻게 구분할 수 있을까요?
- GPU 없이도 1편에서 무엇을 검증할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_groq_baseline_vs_finetuned.py` | 예제 코드 |
| `step02_finetuning_cost_tradeoff_calculator.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-intro/step01_groq_baseline_vs_finetuned.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/01-intro.md)
