# GitHub Actions 101 (9/10): Secret 관리

Github Actions 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- repository, environment, organization secret은 어떻게 구분할까요?
- `GITHUB_TOKEN` 권한은 왜 가능한 한 좁혀야 할까요?
- OIDC는 장기 키 문제를 어떻게 줄여 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2.yaml` | 예제 코드 |
| `3_github_token.yaml` | 예제 코드 |
| `4.yaml` | 예제 코드 |
| `job_matrix.yaml` | 예제 코드 |
| `secret.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-secret-management/2.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/09-secret-management.md)
