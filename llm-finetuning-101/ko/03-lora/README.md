# LLM Fine-tuning 101 (3/6): LoRA 어댑터 구성

Llm Finetuning 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- `LoraConfig`에서 실제로 이해해야 할 필드는 무엇일까요?
- `target_modules`를 잘못 지정하면 어떤 문제가 생길까요?
- 작은 GPT-2 계열 모델에서는 학습 가능한 파라미터 비율이 얼마나 낮아질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_lora_rank_decomposition.py` | 예제 코드 |
| `step02_peft_loraconfig_example.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-lora/step01_lora_rank_decomposition.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/03-lora.md)
