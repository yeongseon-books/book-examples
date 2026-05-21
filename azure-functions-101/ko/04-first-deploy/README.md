# Azure Functions 101 (4/7): 함수 하나 배포하기 — 로컬에서 Azure까지

Azure Functions 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 첫 번째 Function App을 만들기 전에 어떤 파라미터를 먼저 확정해야 할까요?
- zip deploy, GitHub Actions, VS Code 직접 배포 중에서 무엇부터 시작하는 편이 좋을까요?
- Function App은 왜 연결된 Storage Account를 반드시 필요로 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_deploy_plan.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-first-deploy/step01_deploy_plan.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/04-first-deploy.md)
