# LLM from Scratch 101 (5/9): 조립: GPT 모델 클래스 완성

Llm From Scratch 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- GPT 클래스는 어떤 순서로 부품을 호출할까요?
- token embedding과 LM head를 묶는 weight tying은 왜 유용할까요?
- cross-entropy loss는 왜 한 줄 reshape로 계산할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-gpt-model/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/05-gpt-model.md)
