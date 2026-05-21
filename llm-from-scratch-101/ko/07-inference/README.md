# LLM from Scratch 101 (7/9): 샘플링 — 학습된 모델에서 글 뽑아내기

Llm From Scratch 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 생성 루프는 정확히 무엇을 반복할까요?
- greedy decoding은 왜 자주 지루하고 반복적인 출력을 만들까요?
- temperature는 logits 분포를 어떻게 바꿀까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-inference/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/07-inference.md)
