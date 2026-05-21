# LLM from Scratch 101 (6/9): 기울기로 배우기

Llm From Scratch 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 학습 루프를 움직이는 핵심 다섯 줄은 무엇일까요?
- transformer 학습에서 AdamW는 왜 SGD보다 다루기 쉬울까요?
- warmup과 cosine decay는 학습 안정성에 어떤 도움을 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |
| `step_1_train_py.py` | 예제 코드 |
| `step_4.py` | 예제 코드 |
| `warmup_cosine_decay.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-training-loop/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/06-training-loop.md)
