# Korean AI Stack 101 (6/6): 한국어 RAG 파이프라인 조합하기

Korean Ai Stack 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 최소한의 한국어 RAG 파이프라인에서 빠질 수 없는 단계는 무엇일까요?
- 품질 병목은 보통 청킹, 임베딩, 검색, 생성 중 어디에서 가장 자주 생길까요?
- 검색된 문맥은 LLM에 들어가기 전에 어떤 형태로 정리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_faiss_index.py` | 예제 코드 |
| `step02_rag_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-korean-rag-pipeline/step01_faiss_index.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/06-korean-rag-pipeline.md)
