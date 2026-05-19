from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLM


@dataclass
class ChatSession:
    system_prompt: str
    messages: list[dict[str, str]] = field(default_factory=list)

    def send(self, text: str) -> str:
        self.messages.append({"role": "user", "content": text})
        llm = MockLLM()
        resp = llm.chat(self.system_prompt, text)
        choices = cast(list[dict[str, object]], resp["choices"])
        message = cast(dict[str, object], choices[0]["message"])
        answer = str(message["content"])
        self.messages.append({"role": "assistant", "content": answer})
        return answer
