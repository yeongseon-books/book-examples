# Azure App Service Deep Dive (2/6): Front-End과 ARR — 요청은 어떻게 워커에 도달하는가

Azure App Service Deep Dive 시리즈 2편 예제 코드입니다.

## 학습 목표

- Front-End는 단순 로드밸런서를 넘어 실제로 어떤 종류의 결정을 먼저 내릴까요?
- ARR Affinity 쿠키는 애플리케이션 세션 쿠키와 무엇이 다를까요?
- 요청이 어느 앱과 어느 슬롯에 속하는지 정하는 단계와 worker를 고르는 단계는 어떻게 다를까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_arr_affinity_demo.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-app-service-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-front-end-and-arr/step01_arr_affinity_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-app-service-deep-dive/ko/02-front-end-and-arr.md)
