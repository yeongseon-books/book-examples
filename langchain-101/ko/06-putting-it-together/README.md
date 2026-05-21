# LangChain 101 (6/6): 실전 체인 조립 — 컴포넌트를 하나로 연결하기

Langchain 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 하나의 RAG 체인은 문서 인덱싱과 질의 실행을 어떻게 분리해야 할까요?
- retrieval 결과가 비었을 때 모델 호출 전에 어떤 가드를 둘 수 있을까요?
- 스트리밍, 멀티턴 이력, self-contained 앱을 붙여도 구조를 잃지 않으려면 무엇을 기록해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_multiturn_rag_app.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-putting-it-together/step01_multiturn_rag_app.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/06-putting-it-together.md)
