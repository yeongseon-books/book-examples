# Frontend Development 101 (9/10): 빌드 도구와 번들링

Frontend Development 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 번들러는 import 그래프를 따라 어떤 일을 할까요?
- Vite와 esbuild는 왜 빠르다고 평가될까요?
- tree shaking과 dead code elimination은 어떤 비용을 줄여 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `before_after.html` | 예제 코드 |
| `css.css` | 예제 코드 |
| `example.css` | 예제 코드 |
| `example.html` | 예제 코드 |
| `example.js` | 예제 코드 |
| `html.html` | 예제 코드 |
| `javascript.js` | 예제 코드 |
| `presentational_vs_container.js` | 예제 코드 |
| `step01_ep09.py` | 예제 코드 |
| `vite.config.ts` | 예제 코드 |
| `vite.config_13.ts` | 예제 코드 |
| `vite.json` | 예제 코드 |

## 실행 방법

```bash
cd frontend-development-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-build-tools-and-bundling/step01_ep09.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/frontend-development-101/ko/09-build-tools-and-bundling.md)
