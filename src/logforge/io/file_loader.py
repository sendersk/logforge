"""Utilities for reading files."""

from pathlib import Path
from typing import TextIO


class FileLoader:
    """Open text files for reading."""

    def open(self, path: Path) -> TextIO:
        """Open a UTF-8 encoded text file."""

        return path.open(
            mode="r",
            encoding="utf-8",
        )