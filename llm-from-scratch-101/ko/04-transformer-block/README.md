# LLM from Scratch 101 (4/9): 블록 하나, 깊이의 단위

Llm From Scratch 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- FeedForward는 왜 `Linear(C, 4C) -> GELU -> Linear(4C, C)` 형태를 많이 쓸까요?
- residual connection은 학습을 어떻게 안정화할까요?
- pre-norm과 post-norm은 실전에서 어떤 차이를 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |
| `feedforward_mlp.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `surprisingly.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-transformer-block/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/04-transformer-block.md)
