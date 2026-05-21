# LangChain 101 (3/6): Retriever — 문서 검색과 컨텍스트 주입

Langchain 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- Retriever는 VectorStore 검색 결과를 어떻게 LLM 컨텍스트로 바꿀까요?
- 검색 결과가 비어 있거나 엉뚱할 때 모델보다 먼저 어디를 확인해야 할까요?
- VectorStore를 저장하고 다시 불러올 때 어떤 메타데이터가 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_build_faiss.py` | 예제 코드 |
| `step02_rag_chain.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-retriever/step01_build_faiss.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/03-retriever.md)
