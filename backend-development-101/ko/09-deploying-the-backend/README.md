# Backend Development 101 (9/10): 백엔드 배포

Backend Development 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 배포 환경은 어떤 요소들로 이루어질까요?
- Dockerfile은 왜 재현 가능한 실행 환경을 만드는 핵심일까요?
- 환경 변수와 secret은 어떻게 분리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_health_readiness.py` | 예제 코드 |

## 실행 방법

```bash
cd backend-development-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-deploying-the-backend/step01_health_readiness.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/backend-development-101/ko/09-deploying-the-backend.md)
