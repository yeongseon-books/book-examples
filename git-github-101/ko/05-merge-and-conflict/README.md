# Git & GitHub 101 (5/10): merge와 conflict 해결하기 - 두 줄기를 다시 합치기

Git Github 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- fast-forward merge는 언제 일어날까요?
- three-way merge는 왜 부모가 두 개인 commit을 만들까요?
- conflict marker의 `HEAD` 쪽과 incoming branch 쪽은 어떻게 읽을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_merge_conflict.py` | 예제 코드 |

## 실행 방법

```bash
cd git-github-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-merge-and-conflict/step01_merge_conflict.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/git-github-101/ko/05-merge-and-conflict.md)
