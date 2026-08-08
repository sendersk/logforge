"""Tests for file loading."""

from pathlib import Path

import pytest

from logforge.io.exceptions import FileLoadingError
from logforge.io.file_loader import FileLoader


def test_open_existing_file(tmp_path: Path) -> None:
    """Verify that an existing file can be opened."""

    log_file = tmp_path / "application.log"
    log_file.write_text(
        "test log entry\n",
        encoding="utf-8",
    )

    loader = FileLoader()

    with loader.open(log_file) as stream:
        content = stream.read()

    assert content == "test log entry\n"


def test_open_missing_file_raises_erro(tmp_path: Path) -> None:
    """Verify that missing files raise FileLoadingError."""

    missing_file = tmp_path / "missing.log"

    loader = FileLoader()

    with pytest.raises(FileLoadingError):
        loader.open(missing_file)