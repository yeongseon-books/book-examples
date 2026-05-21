# LLM Fine-tuning 101 (2/6): 데이터셋 준비와 전처리

Llm Finetuning 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- `instruction / input / output` 세 필드를 어떤 형태로 잡아야 할까요?
- Hugging Face `datasets`로 작은 JSONL 파일을 어떻게 바로 읽을 수 있을까요?
- 전처리 단계에서 반드시 확인해야 할 최소 검증 포인트는 무엇일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_generate_synthetic_dataset.py` | 예제 코드 |
| `step02_convert_json_to_jsonl_split.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-dataset/step01_generate_synthetic_dataset.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/02-dataset.md)
