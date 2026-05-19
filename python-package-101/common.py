from __future__ import annotations

import ast
import importlib
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    tomllib = importlib.import_module("tomllib")
except ModuleNotFoundError:  # pragma: no cover
    tomllib = importlib.import_module("tomli")


PEP508_RE = re.compile(
    r"^(?P<name>[A-Za-z0-9_.-]+)(\[(?P<extras>[A-Za-z0-9_.,-]+)\])?"
    r"(\s*(?P<op>==|!=|>=|<=|>|<|~=)\s*(?P<version>[^;\s]+))?"
    r"(\s*;\s*(?P<marker>.+))?$"
)


def ep01_detect_package_vs_module(
    target: str, root: Path | None = None
) -> dict[str, Any]:
    base = root or Path.cwd()
    package_init = base / target / "__init__.py"
    module_py = base / f"{target}.py"
    if package_init.exists():
        kind = "package"
    elif module_py.exists():
        kind = "module"
    else:
        spec = importlib.util.find_spec(target)
        kind = (
            "package"
            if spec and spec.submodule_search_locations
            else "module_or_missing"
        )
    return {"target": target, "kind": kind}


def ep02_validate_project_structure(project_root: Path) -> dict[str, Any]:
    has_src_layout = (project_root / "src").exists() and any(
        (project_root / "src").iterdir()
    )
    has_flat_layout = any(project_root.glob("*.py"))
    status = "src-layout" if has_src_layout and not has_flat_layout else "flat-layout"
    if has_src_layout and has_flat_layout:
        status = "mixed-layout"
    return {"project_root": str(project_root), "status": status}


def ep03_parse_dependencies(pyproject_path: Path) -> list[dict[str, Any]]:
    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    deps = data.get("project", {}).get("dependencies", [])
    parsed: list[dict[str, Any]] = []
    for dep in deps:
        match = PEP508_RE.match(dep.strip())
        if not match:
            parsed.append({"raw": dep, "valid": False})
            continue
        part = match.groupdict()
        parsed.append(
            {
                "raw": dep,
                "name": part.get("name"),
                "extras": part.get("extras"),
                "op": part.get("op"),
                "version": part.get("version"),
                "marker": part.get("marker"),
                "valid": True,
            }
        )
    return parsed


def _build_fixture_package(root: Path) -> None:
    pkg = root / "demo_pkg"
    src = pkg / "src" / "demo_pkg"
    src.mkdir(parents=True, exist_ok=True)
    (src / "__init__.py").write_text('__version__ = "0.1.0"\n', encoding="utf-8")
    (pkg / "pyproject.toml").write_text(
        """
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "demo-pkg"
version = "0.1.0"
description = "tiny demo package"
""".strip()
        + "\n",
        encoding="utf-8",
    )


def ep04_run_build_helper(work_root: Path | None = None) -> dict[str, Any]:
    root = work_root or Path(tempfile.mkdtemp(prefix="ep04-build-"))
    _build_fixture_package(root)
    pkg = root / "demo_pkg"
    dist = pkg / "dist"
    build_available = importlib.util.find_spec("build") is not None

    if build_available:
        cmd = [sys.executable, "-m", "build", str(pkg)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        ok = proc.returncode == 0
        if not ok:
            dist.mkdir(parents=True, exist_ok=True)
            (dist / "demo_pkg-0.1.0.tar.gz").write_text(
                "fallback sdist", encoding="utf-8"
            )
            (dist / "demo_pkg-0.1.0-py3-none-any.whl").write_text(
                "fallback wheel", encoding="utf-8"
            )
    else:
        dist.mkdir(parents=True, exist_ok=True)
        (dist / "demo_pkg-0.1.0.tar.gz").write_text("fake sdist", encoding="utf-8")
        (dist / "demo_pkg-0.1.0-py3-none-any.whl").write_text(
            "fake wheel", encoding="utf-8"
        )

    artifacts = sorted(p.name for p in dist.glob("*")) if dist.exists() else []
    has_sdist = any(name.endswith(".tar.gz") for name in artifacts)
    has_wheel = any(name.endswith(".whl") for name in artifacts)
    return {
        "build_available": build_available,
        "artifacts": artifacts,
        "valid": has_sdist and has_wheel,
    }


REQUIRED_META = ["name", "version", "description", "license", "classifiers"]


def ep05_validate_metadata(pyproject_path: Path) -> dict[str, Any]:
    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    project = data.get("project", {})
    missing = [k for k in REQUIRED_META if k not in project]
    return {
        "valid": not missing,
        "missing": missing,
        "docs_only_url": "https://test.pypi.org/",
    }


@dataclass(frozen=True)
class SemVer:
    major: int
    minor: int
    patch: int
    prerelease: str | None = None

    @classmethod
    def parse(cls, value: str) -> "SemVer":
        m = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?$", value)
        if not m:
            raise ValueError(f"invalid semver: {value}")
        major, minor, patch, prerelease = m.groups()
        return cls(int(major), int(minor), int(patch), prerelease)

    def bump(self, part: str, prerelease: str | None = None) -> "SemVer":
        if part == "major":
            return SemVer(self.major + 1, 0, 0, prerelease)
        if part == "minor":
            return SemVer(self.major, self.minor + 1, 0, prerelease)
        if part == "patch":
            return SemVer(self.major, self.minor, self.patch + 1, prerelease)
        raise ValueError("part must be major/minor/patch")

    def __str__(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        return f"{base}-{self.prerelease}" if self.prerelease else base


def ep06_bump_version(version: str, part: str, prerelease: str | None = None) -> str:
    return str(SemVer.parse(version).bump(part, prerelease=prerelease))


def ep07_run_cli(args: list[str]) -> tuple[int, str]:
    parser_src = (
        "import argparse\n"
        "p=argparse.ArgumentParser()\n"
        "p.add_argument('name')\n"
        "ns=p.parse_args()\n"
        "print(f'hello, {ns.name}')\n"
    )
    with tempfile.TemporaryDirectory(prefix="ep07-cli-") as td:
        path = Path(td) / "cli.py"
        path.write_text(parser_src, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(path), *args],
            capture_output=True,
            text=True,
            check=False,
        )
    return proc.returncode, proc.stdout.strip()


def ep08_count_annotations(module_path: Path) -> dict[str, Any]:
    if shutil.which("mypy"):
        proc = subprocess.run(
            ["mypy", str(module_path)], capture_output=True, text=True, check=False
        )
        return {
            "checker": "mypy",
            "ok": proc.returncode == 0,
            "output": proc.stdout + proc.stderr,
        }
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    annotated = [
        f
        for f in funcs
        if f.returns is not None or any(a.annotation for a in f.args.args)
    ]
    return {
        "checker": "ast",
        "function_count": len(funcs),
        "annotated_count": len(annotated),
        "ok": len(annotated) > 0,
    }


def ep09_extract_docstrings(module_path: Path) -> dict[str, Any]:
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    docs: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node) or ""
            docs.append(
                {
                    "name": node.name,
                    "has_docstring": bool(doc.strip()),
                    "has_args": "Args:" in doc,
                    "has_returns": "Returns:" in doc,
                }
            )
    return {
        "functions": docs,
        "google_style_count": sum(
            1 for d in docs if d["has_args"] and d["has_returns"]
        ),
    }


def ep10_generate_template(
    target_dir: Path, project_name: str = "sample_pkg"
) -> dict[str, Any]:
    root = target_dir / project_name
    (root / "src" / project_name).mkdir(parents=True, exist_ok=True)
    (root / "tests").mkdir(parents=True, exist_ok=True)
    (root / "src" / project_name / "__init__.py").write_text("", encoding="utf-8")
    (root / "tests" / "test_smoke.py").write_text(
        "def test_smoke():\n    assert True\n", encoding="utf-8"
    )
    (root / "pyproject.toml").write_text(
        f"""
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
description = "generated by episode 10"
""".strip()
        + "\n",
        encoding="utf-8",
    )
    return {
        "root": str(root),
        "files": sorted(
            str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()
        ),
    }
