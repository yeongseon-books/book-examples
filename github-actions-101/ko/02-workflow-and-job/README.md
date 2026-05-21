# GitHub Actions 101 (2/10): Workflow와 Job

Github Actions 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- Workflow, Job, Step은 각각 무엇을 담당할까요?
- `needs`는 왜 단순한 옵션이 아니라 파이프라인 설계 도구일까요?
- `matrix`는 언제 유용하고 언제 비용 폭탄이 될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.yaml` | 예제 코드 |
| `2_needs.yaml` | 예제 코드 |
| `3_matrix.yaml` | 예제 코드 |
| `4_outputs.yaml` | 예제 코드 |
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
python ko/02-workflow-and-job/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/02-workflow-and-job.md)
