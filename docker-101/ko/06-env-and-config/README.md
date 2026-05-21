# Docker 101 (6/10): 환경변수와 설정

Docker 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 하나의 이미지로 여러 환경을 어떻게 지원할 수 있을까요?
- `ENV`와 `ARG`는 무엇이 다를까요?
- 환경변수, 설정 파일, secret은 어떻게 구분하는 편이 좋을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_env_config_validate.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-env-and-config/step01_env_config_validate.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/06-env-and-config.md)
