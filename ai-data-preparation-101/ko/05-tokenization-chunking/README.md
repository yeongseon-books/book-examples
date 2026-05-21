# AI Data Preparation 101 (5/10): Tokenization과 Chunking 전략

Ai Data Preparation 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 왜 같은 의미의 한국어 문장이 영어보다 더 많은 토큰을 쓰는 경우가 많을까요?
- BPE, WordPiece, SentencePiece는 어떤 기준으로 선택해야 할까요?
- 도메인 전용 모델에서 자체 토크나이저 학습이 가치 있는 순간은 언제일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_token_chunk.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-tokenization-chunking/step01_token_chunk.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/05-tokenization-chunking.md)
