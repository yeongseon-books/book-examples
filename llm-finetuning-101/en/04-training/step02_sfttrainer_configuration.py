"""SFTTrainer configuration example"""

# pyright: reportMissingImports=false, reportOptionalCall=false, reportOptionalMemberAccess=false

from __future__ import annotations

try:
    from peft import LoraConfig, TaskType
except ImportError as exc:
    LoraConfig = None
    TaskType = None
    PEFT_IMPORT_ERROR = exc
else:
    PEFT_IMPORT_ERROR = None

try:
    from trl import SFTTrainer
except ImportError as exc:
    SFTTrainer = None
    TRL_IMPORT_ERROR = exc
else:
    TRL_IMPORT_ERROR = None

try:
    from transformers import TrainingArguments
except ImportError as exc:
    TrainingArguments = None
    TRANSFORMERS_IMPORT_ERROR = exc
else:
    TRANSFORMERS_IMPORT_ERROR = None


def main() -> None:
    training_args_kwargs = {
        'output_dir': './artifacts/sft-demo',
        'per_device_train_batch_size': 2,
        'gradient_accumulation_steps': 8,
        'learning_rate': 2e-4,
        'num_train_epochs': 3,
        'logging_steps': 10,
        'save_steps': 50,
        'bf16': False,
    }

    lora_kwargs = {
        'r': 8,
        'lora_alpha': 16,
        'lora_dropout': 0.05,
        'target_modules': ['q_proj', 'v_proj'],
        'bias': 'none',
    }

    if None in (LoraConfig, TaskType, SFTTrainer, TrainingArguments):
        print('Optional libraries are missing, so only the configuration example is printed.')
        print({
            'peft_error': str(PEFT_IMPORT_ERROR),
            'trl_error': str(TRL_IMPORT_ERROR),
            'transformers_error': str(TRANSFORMERS_IMPORT_ERROR),
            'training_args': training_args_kwargs,
            'lora': lora_kwargs,
            'trainer_class': 'trl.SFTTrainer',
        })
        return

    training_args = TrainingArguments(**training_args_kwargs)
    lora_config = LoraConfig(task_type=TaskType.CAUSAL_LM, **lora_kwargs)
    print('Prepared runnable configuration objects. Attach a real model and dataset to train.')
    print(training_args)
    print(lora_config)
    print(SFTTrainer)


if __name__ == '__main__':
    main()
