# GitHub Actions 101 (1/10): GitHub Actions란 무엇인가?

Github Actions 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- GitHub Actions는 정확히 무엇이고 CI/CD에서 어디에 놓일까요?
- Workflow, Job, Step은 어떤 계층 구조로 이해해야 할까요?
- 첫 워크플로우는 어떤 최소 구성으로 시작하는 편이 좋을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `ci.yml` | 예제 코드 |
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
python ko/01-what-is-github-actions/ci.yml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/01-what-is-github-actions.md)
