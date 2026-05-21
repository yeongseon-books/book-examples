# pipeline.py
import hashlib
import pathlib

import pandas as pd
import yaml


class Stage:
    name: str
    inputs: list[str]
    outputs: list[str]
    params: dict

    def fingerprint(self) -> str:
        h = hashlib.sha256()
        h.update(self.name.encode())
        for p in sorted(self.inputs):
            h.update(pathlib.Path(p).read_bytes())
        h.update(yaml.safe_dump(self.params, sort_keys=True).encode())
        return h.hexdigest()[:12]

    def is_cached(self) -> bool:
        manifest = pathlib.Path(f"manifests/{self.name}.yaml")
        if not manifest.exists():
            return False
        return yaml.safe_load(manifest.read_text())["fingerprint"] == self.fingerprint()

    def run(self):
        if self.is_cached():
            print(f"[skip] {self.name} cached")
            return
        self.execute()  # implemented by subclass
        self.write_manifest()
