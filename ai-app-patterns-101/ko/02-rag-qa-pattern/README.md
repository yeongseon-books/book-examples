# AI App Patterns 101 (2/6): RAG Q&A 패턴 — 문서 기반 질의응답

Ai App Patterns 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- RAG 답변 품질을 보기 전에 왜 검색 결과부터 확인해야 할까요?
- 근거가 약한데도 모델이 답하게 두면 어떤 실패가 생길까요?
- 출처를 함께 반환하려면 청크와 메타데이터를 어디서 보존해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_basic_rag.py` | 예제 코드 |
| `step02_rag_with_sources.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-app-patterns-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-rag-qa-pattern/step01_basic_rag.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-app-patterns-101/ko/02-rag-qa-pattern.md)
