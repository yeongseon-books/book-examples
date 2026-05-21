# Alembic 101 (9/10): 배포 순서와 blue/green: schema와 application code의 안전한 동기화

Alembic 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- migration-first와 code-first deploy ordering은 어떻게 다를까요?
- 왜 blue/green deploy는 두 앱 버전과 동시에 호환되는 schema를 요구할까요?
- NOT NULL 강화는 왜 두 단계로 나눠야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_deploy_ordering.py` | 예제 코드 |

## 실행 방법

```bash
cd alembic-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-deploy-ordering-and-blue-green/step01_deploy_ordering.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/alembic-101/ko/09-deploy-ordering-and-blue-green.md)
