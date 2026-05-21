# Kubernetes 101 (9/10): Helm

Kubernetes 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 환경마다 YAML을 복사하는 방식은 왜 드리프트를 만들까요?
- Chart와 `values.yaml`은 어떤 책임을 나눌까요?
- `install`, `upgrade`, `rollback`은 어떤 흐름으로 이어질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1.py` | 예제 코드 |
| `2_values_yaml.py` | 예제 코드 |
| `3.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `5.py` | 예제 코드 |
| `chart-template.yaml` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-helm/1.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/09-helm.md)
