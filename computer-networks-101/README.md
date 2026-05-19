# computer-networks-101 예제 코드

`computer-networks-101` 시리즈의 에피소드별 오프라인 예제 코드 저장소입니다. 모든 예제는 오프라인(localhost/순수 Python)으로 실행됩니다.

## 구성

- 01: what-is-a-network
- 02: ip-and-subnet
- 03: tcp-and-udp
- 04: dns
- 05: http-and-https
- 06: tls-basics
- 07: routing-and-nat
- 08: load-balancer
- 09: websocket-and-realtime
- 10: debugging-network-problems

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-a-network.py
python en/10-debugging-network-problems.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/computer-networks-101
