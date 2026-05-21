# Vector Search 101 (2/6): HuggingFace 임베딩 실습 — sentence-transformers로 첫 벡터 만들기

Vector Search 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- sentence-transformers로 만든 벡터가 정말 검색에 쓸 수 있는 형태인지 어디서 확인할까요?
- 한 문장씩 인코딩하는 코드와 배치 인코딩 코드는 운영에서 어떤 차이를 만들까요?
- 벡터를 저장했다가 다시 불러올 때 무엇을 함께 기록해야 나중에 재현할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_batch_embeddings.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-huggingface-embeddings/step01_batch_embeddings.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/02-huggingface-embeddings.md)
