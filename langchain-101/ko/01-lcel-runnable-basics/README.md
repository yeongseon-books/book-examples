# LangChain 101 (1/6): LangChain 소개 — LCEL과 Runnable 기본

Langchain 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- LCEL은 프롬프트, 모델, 파서를 어떤 공통 계약으로 묶어 줄까요?
- `prompt | llm | parser` 안에서는 단계마다 어떤 데이터 모양이 오갈까요?
- `invoke()`, `batch()`, `stream()`은 같은 체인에서 각각 언제 써야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_basic_chain.py` | 예제 코드 |
| `step02_runnable_map.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-lcel-runnable-basics/step01_basic_chain.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/01-lcel-runnable-basics.md)
