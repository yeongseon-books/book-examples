# Document Ingestion 101 (1/6): PDF 파싱과 텍스트 추출

Document Ingestion 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- PDF 파일은 왜 단순한 텍스트 파일처럼 읽을 수 없을까요?
- 페이지 구조와 메타데이터를 추출 단계에서 보존하지 않으면 RAG에서 무엇이 막힐까요?
- 파싱 결과가 좋아 보일 때도 어떤 검증을 먼저 해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_pymupdf_basics.py` | 예제 코드 |
| `step02_pdf_metadata.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-pdf-parsing/step01_pymupdf_basics.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/01-pdf-parsing.md)
