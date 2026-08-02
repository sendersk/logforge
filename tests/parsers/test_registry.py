from pathlib import Path

import pytest

from logforge.parsers.base import BaseParser
from logforge.parsers.exceptions import UnsupportedFileTypeError
from logforge.parsers.registry import ParserRegistry


class DummyParser(BaseParser):
    """Dummy parser used for testing."""

    def parse(self, path: Path):
        return []


def test_registry_returns_registered_parser() -> None:
    registry = ParserRegistry()

    parser = DummyParser()

    registry.register(".log", parser)

    assert registry.get(Path("app.log")) is parser


def test_registry_raises_for_unknown_extension() -> None:
    registry = ParserRegistry()

    with pytest.raises(UnsupportedFileTypeError):
        registry.get(Path("app.unknown"))