import json
import subprocess
import sys
from pathlib import Path


def test_preprocessing_preserves_untyped_request_bodies(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    spec = {
        "paths": {
            "/example": {
                "post": {
                    "requestBody": {"content": {"application/json": {"example": {"name": "test"}}}},
                    "responses": {},
                }
            }
        }
    }
    source, output = tmp_path / "source.json", tmp_path / "output.json"
    source.write_text(json.dumps(spec))
    subprocess.run([sys.executable, root / "scripts/preprocess.py", source, output], check=True)
    media = json.loads(output.read_text())["paths"]["/example"]["post"]["requestBody"]["content"]["application/json"]
    assert media["schema"] == {}
    assert media["example"] == {"name": "test"}


def test_generator_fix_imports_missing_unset_without_changing_existing_imports(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    generated = tmp_path / "api" / "example.py"
    generated.parent.mkdir()
    generated.write_text("from ...types import UNSET, Response\n\ndef call(value: str | Unset = UNSET):\n    pass\n")
    types = tmp_path / "types.py"
    types.write_text("class Unset:\n    pass\n\nUNSET = Unset()\n")
    subprocess.run([sys.executable, root / "scripts/fix_generated.py", tmp_path], check=True)
    content = generated.read_text()
    assert "from ...types import Unset\n" in content
    assert "from ...types import UNSET, Response\n" in content
    assert types.read_text() == "class Unset:\n    pass\n\nUNSET = Unset()\n"
    subprocess.run([sys.executable, root / "scripts/fix_generated.py", tmp_path], check=True)
    assert generated.read_text() == content
