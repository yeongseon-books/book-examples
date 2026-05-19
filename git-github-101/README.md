# git-github-101

`git-github-101` 시리즈의 예제 코드 저장소입니다. 예제는 오프라인에서 실행되며, 실사용 저장소나 GitHub API를 건드리지 않도록 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/02-first-commit/step01_first_commit.py
python -m pytest tests/ -q
```

## 안전 원칙

- Git CLI를 사용하는 예제는 항상 `tempfile.mkdtemp()`로 만든 임시 저장소에서만 실행합니다.
- 예제 스크립트는 사용자 저장소 경로로 `cd`하지 않습니다.
- GitHub API/`gh` CLI 호출 없이 in-memory mock 모델로 PR/Issue/Workflow를 시뮬레이션합니다.

## 디렉터리

- `common.py`: 임시 저장소 helper, safe git wrapper, MiniRepo/PR/Issue/Workflow 모델, commit message linter
- `ko/`: 한국어 에피소드별 예제
- `en/`: 영어 미러 예제
- `tests/`: 에피소드별 행동 테스트
