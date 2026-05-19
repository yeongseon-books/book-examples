# linux-cli-101

`linux-cli-101` 시리즈 예제 코드 저장소입니다. 모든 에피소드는 오프라인에서 안전하게 실행되는 Python 예제로 구성되어 있습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-cli-and-shell/step01_cli_shell.py
python en/10-ssh-and-remote/step01_ssh_sim.py
pytest -q
```

## 구성

- `common.py`: `make_temp_workspace()`, `run_cmd()`, `ProcessManager`, `EnvScope`, `SSHSimulator`
- `ko/`, `en/`: 10개 에피소드 예제 코드 (동일 구조)
- `tests/`: 에피소드별 행동 테스트

## 안전 정책

- 파일 시스템 실습은 모두 `tempfile.mkdtemp()` 기반 임시 작업공간에서만 수행합니다.
- 사용자 홈/시스템 경로를 수정하지 않습니다.
- SSH는 실제 연결 없이 `SSHSimulator`로만 시뮬레이션합니다.
