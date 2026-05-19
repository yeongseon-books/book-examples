from __future__ import annotations

import hashlib
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import PurePosixPath

FileSystem = dict[str, str]


def normalize_path(path: str) -> str:
    return str(PurePosixPath("/" + path.lstrip("/")))


def compute_digest(payload: str) -> str:
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Layer:
    name: str
    files: Mapping[str, str]

    def digest(self) -> str:
        items = sorted((normalize_path(k), v) for k, v in self.files.items())
        rendered = "\n".join(f"{k}={v}" for k, v in items)
        return compute_digest(rendered)


def flatten_layers(layers: Iterable[Layer]) -> FileSystem:
    fs: FileSystem = {}
    for layer in layers:
        for path, content in layer.files.items():
            p = normalize_path(path)
            if content == "__DELETE__":
                fs.pop(p, None)
            else:
                fs[p] = content
    return fs
