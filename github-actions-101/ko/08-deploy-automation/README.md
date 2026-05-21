# GitHub Actions 101 (8/10): 배포 자동화

Github Actions 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- staging 자동 배포와 production 승인 게이트는 어떻게 나눌까요?
- GitHub Environments는 왜 배포 정책의 중심이 될까요?
- OIDC는 장기 클라우드 키를 어떻게 대체할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_staging.yaml` | 예제 코드 |
| `3_production.yaml` | 예제 코드 |
| `4_oidc.yaml` | 예제 코드 |
| `5.yaml` | 예제 코드 |
| `job_matrix.yaml` | 예제 코드 |
| `secret.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd github-actions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-deploy-automation/2_staging.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/github-actions-101/ko/08-deploy-automation.md)
