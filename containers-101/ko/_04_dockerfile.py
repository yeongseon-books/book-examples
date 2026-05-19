from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Instruction:
    opcode: str
    args: str


def parse_dockerfile(source: str) -> list[Instruction]:
    out: list[Instruction] = []
    for raw in source.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(maxsplit=1)
        out.append(Instruction(parts[0].upper(), parts[1] if len(parts) > 1 else ''))
    return out


def lint_dockerfile(source: str) -> list[str]:
    warnings: list[str] = []
    has_user = False
    for ins in parse_dockerfile(source):
        if ins.opcode == 'FROM' and ':' not in ins.args:
            warnings.append('Base image tag must be pinned')
        if ins.opcode == 'FROM' and ins.args.endswith(':latest'):
            warnings.append('Avoid latest tag for base image')
        if ins.opcode == 'RUN' and 'pip install' in ins.args and '--no-cache-dir' not in ins.args:
            warnings.append('Use --no-cache-dir with pip install')
        if ins.opcode == 'USER':
            has_user = True
            if ins.args.strip() == 'root':
                warnings.append('Do not run as root user')
    if not has_user:
        warnings.append('USER directive is missing')
    return warnings
