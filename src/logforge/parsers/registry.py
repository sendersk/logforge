"""Parser registry."""

from pathlib import Path

from logforge.parsers.base import BaseParser
from logforge.parsers.exceptions import UnsupportedFileTypeError


class ParserRegistry:
    """Registry of available parsers."""

    def __init__(self) -> None:
        self._parsers: dict[str, BaseParser] = {}

    def register(self, extension: str, parser: BaseParser) -> None:
        """Register parser for file extension."""
        self._parsers[extension.lower()] = parser

    def get(self, path: Path) -> BaseParser:
        """Return parser for file."""

        extension = path.suffix.lower()

        if extension not in self._parsers:
            raise UnsupportedFileTypeError(
                f"No parser registered for '{extension}'"
            )

        return self._parsers[extension]