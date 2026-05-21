# Korean AI Stack 101 (2/6): KoSimCSE로 문장 유사도 구현하기

Korean Ai Stack 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- KoSimCSE는 한국어 검색 작업에서 어디서 가장 먼저 효과를 냅니까?
- FAQ 질문만 먼저 인덱싱하는 방식이 왜 깔끔한 첫 버전일까요?
- 정규화된 임베딩이 `IndexFlatIP`와 왜 그렇게 잘 맞을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_sentence_similarity.py` | 예제 코드 |
| `step02_semantic_search.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-kosimcse-similarity/step01_sentence_similarity.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/02-kosimcse-similarity.md)
