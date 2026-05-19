# containers-101 예제 코드

Docker 데몬 없이 순수 Python으로 컨테이너 개념을 시뮬레이션합니다.

## 구성

- `common.py`: 레이어/해시 등 공통 유틸리티
- `ko/01-what-is-a-container.py`: 가상 파일시스템 기반 격리 시뮬레이터
- `ko/02-image-and-layer.py`: 레이어 스태킹, COW, digest 계산
- `ko/03-runtime.py`: OCI runtime config.json 부분 검증기
- `ko/04-dockerfile.py`: Dockerfile 파서 + 린터
- `ko/05-volume.py`: 마운트 해석/충돌 검사
- `ko/06-network.py`: 브리지 네트워크/IP 할당/ping 시뮬레이션
- `ko/07-registry.py`: Registry manifest schema 검증기
- `ko/08-container-security.py`: 보안 스캐너
- `ko/09-container-vs-vm.py`: 리소스 오버헤드 시뮬레이터
- `ko/10-build-a-container-app.py`: 엔드투엔드 가상 빌드 파이프라인
- `en/*.py`: `ko/`와 동일 로직의 영어 미러
- `tests/`: 에피소드별 동작 테스트

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-a-container.py
python en/10-build-a-container-app.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/containers-101
