# Azure Container Apps 101 (3/7): 첫 배포하기 — Python/FastAPI

Azure Aca 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 로컬 FastAPI 코드가 실제 ACA Revision으로 살아나기까지의 전체 경로는 어떻게 될까요?
- ACA가 이미지를 직접 빌드해 주지 않는다는 사실은 책임 분담에 어떤 의미를 가질까요?
- ACR → ACA Environment → Container App → Revision이라는 네 단계 의존성 체인은 어떻게 이어질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_first_deploy.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-first-deploy/step01_first_deploy.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/03-first-deploy.md)
