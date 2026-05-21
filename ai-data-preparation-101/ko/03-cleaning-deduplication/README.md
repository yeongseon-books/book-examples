# AI Data Preparation 101 (3/10): 데이터 정제와 중복 제거

Ai Data Preparation 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 정제 함수는 왜 작은 변환들의 합으로 유지해야 할까요?
- exact dedup만으로는 웹 코퍼스 품질 문제가 왜 충분히 해결되지 않을까요?
- MinHash threshold를 너무 낮추거나 높이면 어떤 오류가 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_clean_dedup.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-cleaning-deduplication/step01_clean_dedup.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/03-cleaning-deduplication.md)
