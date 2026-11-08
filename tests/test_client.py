import os
import shutil
import subprocess
from pathlib import Path

import pytest

from qdivzero_py.client import AuthenticatedClient


def test_client_imports() -> None:
    client = AuthenticatedClient(base_url="https://api.qdiv0.com", token="test")
    assert client._base_url == "https://api.qdiv0.com"
    assert client.token == "test"


@pytest.mark.parametrize("generation_fails", [False, True])
def test_update_preserves_handwritten_files(tmp_path: Path, generation_fails: bool) -> None:
    root = Path(__file__).resolve().parents[1]
    (tmp_path / "scripts").mkdir()
    (tmp_path / "api").mkdir()
    (tmp_path / "qdivzero_py").mkdir()
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    shutil.copy2(root / "scripts" / "update.sh", tmp_path / "scripts" / "update.sh")
    shutil.copy2(root / "scripts" / "preprocess.py", tmp_path / "scripts" / "preprocess.py")
    shutil.copy2(root / "scripts" / "fix_generated.py", tmp_path / "scripts" / "fix_generated.py")
    (tmp_path / "api" / "openapi.json").write_text("old")
    (tmp_path / "api" / "opc-config.yaml").write_text('package_version_override: "1.0.0"\n')
    originals = {
        "qdivzero_py/auth.py": "custom auth",
        "qdivzero_py/__init__.py": "custom init",
        "README.md": "custom readme",
        ".gitignore": "custom ignore",
    }
    for path, content in originals.items():
        (tmp_path / path).write_text(content)

    commands = {
        "curl": 'printf \'{"paths":{}}\' > "$4"',
        "openapi-python-client": (
            'for f in qdivzero_py/auth.py qdivzero_py/__init__.py README.md .gitignore; do printf generated > "$f"; done\n'
            'printf "[project]\\ndependencies = [\\n]\\n" > pyproject.toml' + ("\nexit 23" if generation_fails else "")
        ),
        "git": 'if [ "$1" = tag ]; then exit 0; fi; exit 77',
        "ruff": "exit 0",
        "uv": "exit 0",
    }
    for name, body in commands.items():
        command = bin_dir / name
        command.write_text(f"#!/bin/sh\n{body}\n")
        command.chmod(0o755)
    env = dict(os.environ, HOME=str(tmp_path), PATH=f"{bin_dir}:{os.environ['PATH']}")
    result = subprocess.run(["bash", "scripts/update.sh"], cwd=tmp_path, env=env, capture_output=True, text=True)
    assert result.returncode == (23 if generation_fails else 77), result.stdout + result.stderr
    for path, content in originals.items():
        assert (tmp_path / path).read_text() == content
