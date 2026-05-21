# AI Data Preparation 101 (8/10): 데이터 증강 기법 — EDA부터 Back-Translation까지

Ai Data Preparation 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- augmentation은 synthetic generation과 무엇이 다른가요?
- minority class와 typo robustness 문제를 어떤 decision path로 풀어야 하나요?
- EDA, back-translation, paraphrase, AST transform은 각각 언제 선택하고 언제 멈춰야 하나요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_light_augmentation.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-data-augmentation/step01_light_augmentation.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/08-data-augmentation.md)
