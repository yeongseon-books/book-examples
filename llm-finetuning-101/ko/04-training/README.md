# LLM Fine-tuning 101 (4/6): 학습 루프와 하이퍼파라미터

Llm Finetuning 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- `TrainingArguments`에서 한 번의 학습 스텝을 돌리려면 최소 무엇을 설정해야 할까요?
- 작은 실험에서도 `labels`와 데이터 콜레이터가 왜 중요할까요?
- 학습 루프를 디버깅할 때 어떤 출력부터 읽어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_training_loop_simulation.py` | 예제 코드 |
| `step02_sfttrainer_configuration.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-training/step01_training_loop_simulation.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/04-training.md)
