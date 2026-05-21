# AI Data Preparation 101 (6/10): 데이터 품질 필터링 — Heuristic과 Classifier

Ai Data Preparation 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 왜 수집된 데이터와 학습 가능한 데이터는 같은 집합이 아닐까요?
- 길이, symbol ratio, digit ratio, repetition 같은 heuristic signal은 무엇을 빠르게 잡아낼까요?
- 언어 감지와 perplexity filter는 각각 어떤 종류의 오염을 제거할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `cheap_expensive.py` | 예제 코드 |
| `classifier_filter.py` | 예제 코드 |
| `heuristic_filter_signal.py` | 예제 코드 |
| `out_of_domain.py` | 예제 코드 |
| `perplexity_filter.py` | 예제 코드 |
| `step01_heuristic_filter.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-quality-filtering/cheap_expensive.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/06-quality-filtering.md)
