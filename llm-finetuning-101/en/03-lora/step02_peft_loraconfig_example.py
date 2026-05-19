"""PEFT LoraConfig example"""

# pyright: reportMissingImports=false

from __future__ import annotations

try:
    from peft import LoraConfig, TaskType
except ImportError as exc:
    LoraConfig = None
    TaskType = None
    IMPORT_ERROR = exc
else:
    IMPORT_ERROR = None


def main() -> None:
    config_kwargs = {
        'r': 16,
        'lora_alpha': 32,
        'lora_dropout': 0.05,
        'target_modules': ['q_proj', 'k_proj', 'v_proj', 'o_proj'],
        'bias': 'none',
    }

    if LoraConfig is None or TaskType is None:
        print('Skipping real LoraConfig creation because peft is not installed.')
        print('ImportError details', IMPORT_ERROR)
        print(config_kwargs)
        return

    config = LoraConfig(task_type=TaskType.CAUSAL_LM, **config_kwargs)
    print('Created LoraConfig')
    print(config)


if __name__ == '__main__':
    main()
