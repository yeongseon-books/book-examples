# Document Ingestion 101 (5/6): 다중 포맷 문서 파이프라인

Document Ingestion 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- PDF, Markdown, HTML을 한 파이프라인에 넣으려면 무엇을 먼저 공통 계약으로 맞춰야 할까요?
- 파일 형식별 loader routing은 어디까지 분기하고 어디서 다시 합쳐져야 할까요?
- 정규화 계층이 없으면 후속 청킹과 메타데이터 필터링에서 어떤 문제가 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_format_router.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-multi-format-pipeline/step01_format_router.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/05-multi-format-pipeline.md)
