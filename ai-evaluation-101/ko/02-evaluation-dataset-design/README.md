# AI Evaluation 101 (2/10): 평가 데이터셋 설계하기

Ai Evaluation 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 좋은 평가 데이터셋은 왜 모델 시험지가 아니라 운영 표본이어야 할까요?
- 대표 사례와 실패 사례를 어떤 비율로 섞어야 실제 품질 변화를 볼 수 있을까요?
- eval set을 버전 관리하지 않으면 어떤 판단이 흐려질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dataset_mix.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-evaluation-dataset-design/step01_dataset_mix.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/02-evaluation-dataset-design.md)
