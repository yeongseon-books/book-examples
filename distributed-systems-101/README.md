# distributed-systems-101

`distributed-systems-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 in-process mock 기반이며, 에피소드별 핵심 개념을 짧은 코드로 검증하도록 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 에피소드 목록

- 01-what-is-a-distributed-system
- 02-failure-model
- 03-rpc-and-message-passing
- 04-consistency-and-cap
- 05-replication
- 06-consensus-and-raft
- 07-leader-election
- 08-message-queue-and-event-sourcing
- 09-distributed-transaction
- 10-operable-distributed-patterns

## 실행

```bash
python ko/01-what-is-a-distributed-system.py
python en/10-operable-distributed-patterns.py
```

## 테스트 실행

```bash
pytest -q
```

## 디렉토리 맵

- `common.py` - 네트워크, 복제, 합의, 큐, 트랜잭션, 운영 패턴 공통 mock
- `ko/` - 한국어 주석 에피소드별 예제 (01-10)
- `en/` - 영어 주석 에피소드별 예제 (01-10)
- `tests/` - 에피소드별 동작 검증 테스트

## License

MIT
