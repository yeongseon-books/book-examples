# llm-finetuning-101

Step-by-step LLM fine-tuning examples in Korean and English.

## Layout

```text
llm-finetuning-101/
├── ko/
│   ├── 01-intro/
│   ├── 02-dataset/
│   ├── 03-lora/
│   ├── 04-training/
│   ├── 05-evaluation/
│   └── 06-serving/
├── en/
│   ├── 01-intro/
│   ├── 02-dataset/
│   ├── 03-lora/
│   ├── 04-training/
│   ├── 05-evaluation/
│   └── 06-serving/
└── requirements.txt
```

## Notes

- Groq-based steps use `GROQ_API_KEY` from the environment.
- GPU libraries such as `transformers`, `peft`, `trl`, and `bitsandbytes` are optional.
- Scripts that depend on optional GPU libraries use `try/except ImportError` and print guidance instead of crashing.
- Every step is independently runnable.

## Validation

```bash
python3 -m py_compile $(find . -name "*.py")
```
