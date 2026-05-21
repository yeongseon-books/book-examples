# Docker 101 (5/10): Docker Compose

Docker 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 여러 컨테이너를 한 번에 재현 가능하게 실행하려면 무엇이 필요할까요?
- service, network, volume은 Compose에서 어떻게 정의할까요?
- `depends_on`과 healthcheck는 어떤 관계로 이해해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_compose_validate.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-docker-compose/step01_compose_validate.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/05-docker-compose.md)
