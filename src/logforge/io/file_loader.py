"""Utilities for reading files."""

from pathlib import Path
from typing import TextIO

from logforge.io.exceptions import FileLoadingError


class FileLoader:
    """Load text files from the filesystem."""

    def open(self, path: Path) -> TextIO:
        """Open a text file for reading."""
        try:
            return path.open(
                mode="r",
                encoding="utf-8",
            )
        except OSError as error:
            raise FileLoadingError(
                f"Unable to open file: {path}"
            ) from error