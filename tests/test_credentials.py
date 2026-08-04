from pathlib import Path

import pytest

from qdivzero_py.auth import load_credentials


def test_loads_tokens_from_file(tmp_path: Path) -> None:
    creds_dir = tmp_path / ".qdivzero"
    creds_dir.mkdir()
    (creds_dir / "credentials").write_text('{"access_token": "t1", "refresh_token": "r1"}')
    creds = load_credentials(home=tmp_path)
    assert creds == {"email": "", "password": "", "access_token": "t1", "refresh_token": "r1", "api_key": ""}


def test_missing_file_is_empty(tmp_path: Path) -> None:
    assert load_credentials(home=tmp_path) == {
        "email": "",
        "password": "",
        "access_token": "",
        "refresh_token": "",
        "api_key": "",
    }


def test_malformed_file_raises(tmp_path: Path) -> None:
    creds_dir = tmp_path / ".qdivzero"
    creds_dir.mkdir()
    (creds_dir / "credentials").write_text("not json")
    with pytest.raises(ValueError):
        load_credentials(home=tmp_path)
