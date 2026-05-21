# GitHub Actions 101 (6/10): 빌드 아티팩트

Github Actions 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- `upload-artifact`와 `download-artifact`는 각각 언제 쓰일까요?
- 잡 사이에서 결과물을 넘길 때 아티팩트가 왜 유용할까요?
- `retention-days`는 비용과 어떤 관계가 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.yaml` | 예제 코드 |
| `2.yaml` | 예제 코드 |
| `3.yaml` | 예제 코드 |
| `4_release.yaml` | 예제 코드 |
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
python ko/06-build-artifact/step01_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/06-build-artifact.md)
