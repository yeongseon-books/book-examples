# GitHub Actions 101 (4/10): Python 테스트 자동화

Github Actions 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- `setup-python`과 pip 캐시는 왜 함께 다뤄야 할까요?
- `pytest` 결과를 PR 체크와 리포트로 드러내려면 무엇이 필요할까요?
- 커버리지는 왜 숫자 자체보다 추세와 기준이 중요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-python-test-automation/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/04-python-test-automation.md)
