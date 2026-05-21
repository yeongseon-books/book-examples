# GitHub Actions 101 (3/10): Trigger 이해하기

Github Actions 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- push와 pull_request는 어떤 차이로 써야 할까요?
- schedule은 왜 로컬 시간이 아니라 UTC로 이해해야 할까요?
- workflow_dispatch는 언제 유용하고 무엇을 문서화해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_push_pr.yaml` | 예제 코드 |
| `2.yaml` | 예제 코드 |
| `3.yaml` | 예제 코드 |
| `4.yaml` | 예제 코드 |
| `5.yaml` | 예제 코드 |
| `job_matrix.yaml` | 예제 코드 |
| `secret.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `snippet_09.yaml` | 예제 코드 |
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-triggers/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/03-triggers.md)
