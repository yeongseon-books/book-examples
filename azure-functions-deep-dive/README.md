# azure-functions-deep-dive

`azure-functions-deep-dive` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반으로 구성했으며, Azure 호출 없이 핵심 동작을 에피소드별로 검증하도록 설계했습니다.

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
python ko/01-host-bootstrap/step01_host_bootstrap.py
python en/06-cold-start-placeholder/step01_placeholder.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - mock HttpRequest/HttpResponse와 에피소드 공통 유틸리티입니다.
- `ko/` - 한국어 에피소드별 예제입니다.
- `en/` - `ko/`와 동일한 로직의 영어 예제입니다.
- `tests/` - 에피소드별 동작 검증 테스트입니다.

## 에피소드 인덱스

1. [01-host-bootstrap](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/01-host-bootstrap.md)
2. [02-worker-process](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/02-worker-process.md)
3. [03-grpc-event-stream](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/03-grpc-event-stream.md)
4. [04-dispatcher-and-invocation](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/04-dispatcher-and-invocation.md)
5. [05-scaling-internals](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/05-scaling-internals.md)
6. [06-cold-start-placeholder](https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-deep-dive/ko/06-cold-start-placeholder.md)

## 주의사항

- 이 저장소는 학습용 오프라인 mock 전용 예제입니다.
- `az`/`func` 명령은 문자열로만 포함하며 실제 실행하지 않습니다.
- 실제 Azure 리소스나 자격 증명은 필요하지 않습니다.

## License

MIT
