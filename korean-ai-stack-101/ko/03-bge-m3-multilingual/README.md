# Korean AI Stack 101 (3/6): BGE-M3 다국어 임베딩 실전

Korean Ai Stack 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- BGE-M3는 한국어와 영어가 섞인 코퍼스에서 KoSimCSE보다 어디서 강합니까?
- 하나의 모델이 dense, sparse, multi-vector 표현을 동시에 낸다는 말은 무엇을 뜻합니까?
- 다국어 검색 첫 버전에서는 dense만으로도 왜 충분한 경우가 많습니까?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_multilingual_embeddings.py` | 예제 코드 |
| `step02_cross_lingual_search.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-bge-m3-multilingual/step01_multilingual_embeddings.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/03-bge-m3-multilingual.md)
