# Korean AI Stack 101 (1/6): 한국어 임베딩 모델 비교 — KoSimCSE, BGE-M3, Solar

Korean Ai Stack 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 영어 중심 임베딩 모델은 한국어 비중이 높은 데이터에서 어디서 자주 무너질까요?
- 코사인 점수 하나보다 유사 쌍과 무관 쌍 사이의 간격이 왜 더 쓸모 있을까요?
- 한국어 텍스트에 영어 기술 용어가 자주 섞일 때는 무엇부터 시험해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_embedding_similarity.py` | 예제 코드 |
| `step02_embedding_benchmark.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-korean-embedding-models/step01_embedding_similarity.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/01-korean-embedding-models.md)
