# Azure App Service Deep Dive (4/6): 배포와 Kudu — 빌드·동기화·릴리스의 안쪽

Azure App Service Deep Dive 시리즈 4편 예제 코드입니다.

## 학습 목표

- Kudu는 App Service에서 정확히 어떤 공개 표면을 제공할까요?
- ZipDeploy는 단순히 ZIP을 풀어 놓는 동작과 어떻게 다를까요?
- Windows code app의 고전적인 Kudu 경로와 Linux code app의 Oryx 경로는 어디서 갈릴까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_deploy_contract.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-deployment-and-kudu/step01_deploy_contract.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/04-deployment-and-kudu.md)
