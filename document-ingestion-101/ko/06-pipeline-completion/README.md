# Document Ingestion 101 (6/6): 문서 수집 파이프라인 완성

Document Ingestion 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 완성된 문서 수집 파이프라인은 어떤 단계별 검증 체크포인트를 가져야 할까요?
- 파싱, 정규화, 청킹, 인덱싱 중 어디서 실패했는지 어떻게 빠르게 알 수 있을까요?
- 운영에서 재실행 가능한 파이프라인으로 만들려면 어떤 산출물을 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_complete_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd document-ingestion-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-pipeline-completion/step01_complete_pipeline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/document-ingestion-101/ko/06-pipeline-completion.md)
