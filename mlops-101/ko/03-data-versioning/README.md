# MLOps 101 (3/10): 데이터 버전 관리

Mlops 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 왜 코드 버전만으로는 학습 결과를 재현할 수 없을까요?
- DVC와 git-LFS는 어떤 차이로 이해하면 좋을까요?
- 큰 데이터 파일은 git 바깥에 두면서도 어떻게 버전 일관성을 유지할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_data_versioning.py` | 예제 코드 |

## 실행 방법

```bash
cd mlops-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-data-versioning/step01_data_versioning.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/mlops-101/ko/03-data-versioning.md)
