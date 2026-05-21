# Azure Container Apps Deep Dive (4/6): ACA 안의 KEDA — Scale Rule이 만드는 것

Azure Aca Deep Dive 시리즈 4편 예제 코드입니다.

## 학습 목표

- ACA의 scale rule은 KEDA에서 어떤 형태의 제어 루프로 읽는 편이 가장 정확할까요?
- 왜 scale rule은 app-scope가 아니라 revision-scope에 속할까요?
- `minReplicas: 0`이 가능하다는 사실은 스케일 모델을 어떻게 바꿀까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_keda_translation.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-keda-in-aca/step01_keda_translation.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/04-keda-in-aca.md)
