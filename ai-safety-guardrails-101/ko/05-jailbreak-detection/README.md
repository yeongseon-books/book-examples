# AI Safety & Guardrails 101 (5/10): Jailbreak 탐지

Ai Safety Guardrails 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Jailbreak detection은 왜 키워드 차단만으로 부족할까요?
- 정규화, 패턴, embedding, LLM judge는 어떤 층위로 조합해야 할까요?
- 다국어·인코딩 우회 사례는 regression dataset에 어떻게 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_jailbreak_detector.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-jailbreak-detection/step01_jailbreak_detector.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/05-jailbreak-detection.md)
