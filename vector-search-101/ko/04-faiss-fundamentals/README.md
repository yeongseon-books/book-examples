# Vector Search 101 (4/6): FAISS 입문 — 고속 근사 최근접 이웃 검색

Vector Search 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 벡터가 많아질수록 단순 반복 검색은 어디서 한계가 날까요?
- IndexFlatIP와 IndexFlatL2는 어떤 전제에서 선택해야 할까요?
- 인덱스를 저장하고 다시 불러올 때 벡터와 메타데이터를 어떻게 맞춰야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_indexflat_search.py` | 예제 코드 |

## 실행 방법

```bash
cd vector-search-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-faiss-fundamentals/step01_indexflat_search.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/vector-search-101/ko/04-faiss-fundamentals.md)
