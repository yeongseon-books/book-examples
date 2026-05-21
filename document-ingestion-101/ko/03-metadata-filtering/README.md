# Document Ingestion 101 (3/6): 메타데이터 설계와 필터링

Document Ingestion 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 메타데이터 스키마는 왜 임베딩 후가 아니라 수집 단계에서 먼저 설계해야 할까요?
- 필터는 벡터 유사도 검색 전에 후보군을 어떻게 바꿀까요?
- 필수 메타데이터가 빠지면 검색과 출처 표시에 어떤 문제가 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_metadata_schema.py` | 예제 코드 |
| `step02_faiss_filter.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-metadata-filtering/step01_metadata_schema.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/03-metadata-filtering.md)
