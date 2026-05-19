# software-engineering-101

Offline-only Python example code for 10 episodes of the `software-engineering-101` series.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Layout

- `common.py`: shared helpers
- `fixtures/`: sample input files
- `ko/`, `en/`: mirrored episode scripts
- `tests/`: pytest coverage (10+ tests)
