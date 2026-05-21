# Docker 101 (9/10): Image 최적화

Docker 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 멀티스테이지 빌드는 왜 build와 runtime을 분리할까요?
- BuildKit cache mount는 어떤 식으로 재빌드를 빠르게 만들까요?
- slim, alpine, distroless는 각각 어떤 trade-off가 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_image_optimization_sim.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-image-optimization/step01_image_optimization_sim.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/09-image-optimization.md)
