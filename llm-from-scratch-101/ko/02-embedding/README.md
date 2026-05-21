# LLM from Scratch 101 (2/9): 정수에서 벡터로, 그리고 위치

Llm From Scratch 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- `nn.Embedding`은 실제로 어떤 연산을 수행할까요?
- 토큰 임베딩만으로는 왜 충분하지 않을까요?
- 위치 정보는 왜 별도 임베딩으로 다루는 편이 실용적일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |
| `gpt_token_emb_pos_emb.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_03.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-embedding/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/02-embedding.md)
