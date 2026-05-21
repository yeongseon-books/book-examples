# Git & GitHub 101 (3/10): 변경 사항 확인하기 - status, diff, log로 읽기

Git Github 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- `git status`의 긴 출력과 짧은 출력은 각각 무엇을 보여 줄까요?
- `git diff`, `git diff --cached`, `git diff HEAD`는 어느 영역끼리 비교할까요?
- 두 commit을 직접 비교할 때는 어떤 순서로 hash를 넣어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_status_diff_log.py` | 예제 코드 |

## 실행 방법

```bash
cd git-github-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-status-diff-log/step01_status_diff_log.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/git-github-101/ko/03-status-diff-log.md)
