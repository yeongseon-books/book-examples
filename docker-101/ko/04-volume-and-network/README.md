# Docker 101 (4/10): Volume과 Network

Docker 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- volume, bind mount, tmpfs는 각각 언제 써야 할까요?
- 컨테이너 데이터는 왜 기본적으로 휘발된다고 봐야 할까요?
- 브리지 네트워크는 어떻게 컨테이너 이름 기반 통신을 가능하게 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_volume_network_sim.py` | 예제 코드 |

## 실행 방법

```bash
cd docker-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-volume-and-network/step01_volume_network_sim.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/docker-101/ko/04-volume-and-network.md)
