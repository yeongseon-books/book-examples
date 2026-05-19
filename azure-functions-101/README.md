# azure-functions-101

`azure-functions-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반이며, 실제 Azure 리소스 호출 없이 동작합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-azure-functions/step01_hello_http.py
python en/07-monitoring-and-ops/step01_monitoring_queries.py
python3 -m pytest tests/ -q
```

## 에피소드 인덱스

- 01: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/01-what-is-azure-functions.md
- 02: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/02-triggers-and-bindings.md
- 03: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/03-host-and-worker.md
- 04: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/04-first-deploy.md
- 05: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/05-choosing-a-plan.md
- 06: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/06-scaling-and-cold-start.md
- 07: https://github.com/yeongseon-books/book-content/blob/master/content/azure-functions-101/ko/07-monitoring-and-ops.md

## 디렉토리 맵

- `common.py` - 오프라인 mock 요청/응답 모델
- `ko/` - 한국어 에피소드별 예제 (01-07)
- `en/` - `ko/`와 동일 로직의 영어 경로 예제
- `tests/` - 에피소드별 동작 테스트

## 주의사항

- 본 저장소는 오프라인 학습용입니다.
- `az`, `func` 명령은 문자열로만 다루며 실제 실행하지 않습니다.
- 실제 Azure 자격 증명, 구독, 네트워크 연결을 요구하지 않습니다.

## License

MIT
