# GitHub Actions 101 (5/10): Lint와 Type Check

Github Actions 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Ruff는 왜 여러 도구를 하나로 줄이는 데 유용할까요?
- Mypy는 어느 시점부터 엄격 모드로 가져가는 편이 좋을까요?
- pre-commit은 왜 CI와 짝을 이뤄야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-lint-and-typecheck/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/05-lint-and-typecheck.md)
