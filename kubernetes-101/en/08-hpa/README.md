# Kubernetes 101 (8/10): HPA

Example code for Kubernetes 101 series, episode 8.

## Learning Goals

- Understand the core concepts of HPA.

## Assets

| File | Description |
|------|-------------|
| `hpa.yaml` | Example code |
| `step01.py` | Example code |
| `step_1_resource_requests_on_the_deployme.py` | Example code |
| `step_2_hpa_manifest.py` | Example code |
| `step_3_apply.py` | Example code |
| `step_4_generate_load.py` | Example code |
| `step_5_inspect_hpa_state.py` | Example code |

## How to Run

```bash
cd kubernetes-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python en/08-hpa/step01.py
```

## Related Article

- [Read the article](https://github.com/yeongseon-books/book-content/blob/main/content/kubernetes-101/en/08-hpa.md)
