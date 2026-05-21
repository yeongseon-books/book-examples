# Document Ingestion 101 (4/6): 증분 인덱싱 — 변경된 문서만 업데이트

Document Ingestion 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 문서가 조금 바뀔 때마다 전체 인덱스를 다시 만들면 어떤 비용이 생길까요?
- 변경 감지는 파일 시간보다 왜 content hash와 상태 저장소가 더 안전할까요?
- 삭제된 문서와 수정된 청크를 인덱스에서 어떻게 구분해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_change_detection.py` | 예제 코드 |
| `step02_incremental_indexer.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-incremental-indexing/step01_change_detection.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/04-incremental-indexing.md)
