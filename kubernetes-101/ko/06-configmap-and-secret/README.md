# Kubernetes 101 (6/10): ConfigMap과 Secret

Kubernetes 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 이미지 안에 설정과 비밀번호를 같이 넣으면 왜 운영이 어려워질까요?
- ConfigMap과 Secret은 무엇이 다르고 어디서 나뉠까요?
- 환경 변수 주입과 파일 마운트는 언제 다르게 선택할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `config-secret.yaml` | 예제 코드 |
| `step01.py` | 예제 코드 |

## 실행 방법

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-configmap-and-secret/config-secret.yaml
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/ko/06-configmap-and-secret.md)
