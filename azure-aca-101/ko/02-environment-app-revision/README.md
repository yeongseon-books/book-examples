# Azure Container Apps 101 (2/7): Environment, Container App, Revision — ACA in three words

Azure Aca 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- ACA의 세 가지 운영 단위인 Environment, Container App, Revision은 정확히 어떤 책임을 가질까요?
- 어떤 변경은 새 Revision을 만들고, 어떤 변경은 만들지 않을까요?
- Single Revision mode와 Multiple Revision mode는 무엇이 다르고, 각각 언제 맞을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_revision_model.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-environment-app-revision/step01_revision_model.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/02-environment-app-revision.md)
