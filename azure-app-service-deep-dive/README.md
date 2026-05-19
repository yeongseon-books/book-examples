# azure-app-service-deep-dive

`azure-app-service-deep-dive` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반이며, Azure 자원 호출 없이 App Service 내부 동작 개념을 에피소드별로 검증하도록 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-platform-architecture/step01_architecture_map.py
python en/06-cold-start-and-warmup/step01_warmup_contract.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - 공통 App Service 개념 모델과 오프라인 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-06)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 에피소드 인덱스

1. [01-platform-architecture.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/01-platform-architecture.md)
2. [02-front-end-and-arr.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/02-front-end-and-arr.md)
3. [03-worker-and-sandbox.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/03-worker-and-sandbox.md)
4. [04-deployment-and-kudu.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/04-deployment-and-kudu.md)
5. [05-scaling-internals.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/05-scaling-internals.md)
6. [06-cold-start-and-warmup.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-deep-dive/ko/06-cold-start-and-warmup.md)

## 주의사항

- 이 저장소는 학습용 오프라인 mock 예제입니다.
- `az` 명령은 문자열/계획 생성 예시만 포함하며 실행하지 않습니다.
- 실제 Azure 구독, 자격 증명, 외부 네트워크 의존성이 없습니다.

## License

MIT
