# Azure Functions 101 (6/7): 스케일링과 콜드 스타트 — 서버리스가 빨라지는 순간과 느려지는 순간

Azure Functions 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- Functions scale controller는 어떤 신호를 보고 인스턴스를 추가할까요?
- 콜드 스타트는 정확히 어느 단계에서 발생하고, 무엇을 측정해야 볼 수 있을까요?
- Premium의 Always Ready나 Flex의 always-ready 인스턴스는 콜드 스타트를 어디까지 줄여 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_scale_simulator.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-scaling-and-cold-start/step01_scale_simulator.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/06-scaling-and-cold-start.md)
