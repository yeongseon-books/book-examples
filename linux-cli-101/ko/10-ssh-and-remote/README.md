# Linux CLI 101 (10/10): SSH와 원격 서버 접속

Linux Cli 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- SSH는 Telnet 대신 왜 기본 원격 접속 수단이 되었을까요?
- 비밀번호 인증과 키 기반 인증은 어떤 차이를 만들까요?
- `~/.ssh/config`는 접속 흐름을 어떻게 단순하게 만들까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ssh_sim.py` | 예제 코드 |

## 실행 방법

```bash
cd linux-cli-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-ssh-and-remote/step01_ssh_sim.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/linux-cli-101/ko/10-ssh-and-remote.md)
