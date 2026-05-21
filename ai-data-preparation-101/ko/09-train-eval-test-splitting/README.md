# AI Data Preparation 101 (9/10): 학습/평가/테스트 분할과 Contamination 통제

Ai Data Preparation 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 단순 `train_test_split`이 실제 운영 조건을 놓치는 대표적인 경우는 무엇일까요?
- 클래스 불균형, 사용자 누수, 시계열 데이터는 왜 서로 다른 split 전략을 요구할까요?
- LLM benchmark contamination은 기존 데이터 누수와 무엇이 다르고 왜 더 위험할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `contamination.py` | 예제 코드 |
| `contamination_llm.py` | 예제 코드 |
| `split.py` | 예제 코드 |
| `split_02.py` | 예제 코드 |
| `split_03.py` | 예제 코드 |
| `split_04.py` | 예제 코드 |
| `step01_stratified_split.py` | 예제 코드 |
| `temporal_group_stratify.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-train-eval-test-splitting/contamination.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/09-train-eval-test-splitting.md)
